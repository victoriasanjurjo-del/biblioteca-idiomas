/**
 * ui.js — Manejador de la interfaz de usuario, renderizado de componentes y eventos
 */

import { Storage, LANGUAGE_FLAGS, DEFAULT_FLAG, getFlag } from './storage.js';
import { Markdown } from './markdown.js';
import { Speech } from './speech.js';

export const UI = {
  // Estado actual de la UI
  state: {
    currentLanguageId: null,
    currentCategory: 'palabras', // 'palabras' | 'frases' | 'textos'
    currentEntryId: null,
    searchQuery: '',
    view: 'list', // 'list' | 'editor' | 'flashcards'
    flashcardIndex: 0,
    flashcardList: [],
    editorMode: 'split', // 'split' | 'edit' | 'preview'
    autoSaveTimeout: null
  },

  // Inicialización de la UI
  init() {
    this.bindGlobalEvents();
    this.initTheme();
    this.renderLanguages();
    
    // Seleccionar primer idioma por defecto si existe
    const languages = Storage.getLanguages();
    if (languages.length > 0) {
      this.selectLanguage(languages[0].id);
    } else {
      this.renderWelcome();
    }
  },

  // Enlazar eventos globales del DOM
  bindGlobalEvents() {
    // Tema claro / oscuro
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) {
      themeBtn.addEventListener('click', () => this.toggleTheme());
    }

    // Menú móvil
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const sidebar = document.getElementById('sidebar');
    const sidebarOverlay = document.getElementById('sidebar-overlay');
    
    if (mobileMenuBtn && sidebar && sidebarOverlay) {
      mobileMenuBtn.addEventListener('click', () => {
        sidebar.classList.toggle('open');
        sidebarOverlay.classList.toggle('open');
      });
      sidebarOverlay.addEventListener('click', () => {
        sidebar.classList.remove('open');
        sidebarOverlay.classList.remove('open');
      });
    }

    // Búsqueda en tiempo real
    const searchInput = document.getElementById('global-search');
    const searchClear = document.getElementById('search-clear-btn');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        this.state.searchQuery = e.target.value.trim().toLowerCase();
        if (searchClear) {
          searchClear.classList.toggle('visible', this.state.searchQuery.length > 0);
        }
        if (this.state.view === 'list') {
          this.renderContentList();
        }
      });
    }
    if (searchClear && searchInput) {
      searchClear.addEventListener('click', () => {
        searchInput.value = '';
        this.state.searchQuery = '';
        searchClear.classList.remove('visible');
        if (this.state.view === 'list') {
          this.renderContentList();
        }
      });
    }

    // Botones para abrir modales de creación
    document.getElementById('btn-new-language')?.addEventListener('click', () => this.openNewLanguageModal());
    document.getElementById('btn-new-entry-hero')?.addEventListener('click', () => this.openNewEntryModal());
    document.getElementById('btn-new-entry-tab')?.addEventListener('click', () => this.openNewEntryModal());

    // Botón de práctica / flashcards
    document.getElementById('btn-practice')?.addEventListener('click', () => this.startPracticeMode());

    // Botones de Backup y Exportación
    document.getElementById('btn-export-json')?.addEventListener('click', () => Storage.exportJSON());
    document.getElementById('btn-import-json')?.addEventListener('click', () => this.openImportModal());

    // Tabs de categoría
    document.querySelectorAll('.category-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        const cat = tab.dataset.category;
        this.selectCategory(cat);
      });
    });

    // Barra de herramientas del editor Markdown
    document.querySelectorAll('.toolbar-btn[data-format]').forEach(btn => {
      btn.addEventListener('click', () => {
        const textarea = document.getElementById('editor-content-input');
        if (textarea) {
          Markdown.insertFormatting(textarea, btn.dataset.format);
          this.handleEditorChange();
        }
      });
    });

    // Cambio de vista del editor (Split / Solo Editar / Solo Previsualizar)
    document.querySelectorAll('.editor-view-toggle').forEach(btn => {
      btn.addEventListener('click', () => {
        const mode = btn.dataset.mode;
        this.setEditorViewMode(mode);
      });
    });

    // Input en tiempo real del editor
    const editorTextarea = document.getElementById('editor-content-input');
    if (editorTextarea) {
      editorTextarea.addEventListener('input', () => this.handleEditorChange());
    }

    // Botón volver del editor
    document.getElementById('btn-editor-back')?.addEventListener('click', () => {
      this.switchView('list');
      this.renderContentList();
      this.renderLanguages(); // Para refrescar conteos
    });

    // Botón guardar manual
    document.getElementById('btn-editor-save')?.addEventListener('click', () => this.saveCurrentEditorEntry());

    // Botón descargar markdown desde editor
    document.getElementById('btn-editor-download')?.addEventListener('click', () => {
      const entry = this.getCurrentEntry();
      if (entry) {
        Storage.downloadMarkdownFile(entry.slug || entry.title, entry.body);
        this.showToast('Archivo Markdown descargado', 'success');
      }
    });

    // Pronunciación en el editor
    document.getElementById('btn-editor-speak')?.addEventListener('click', () => {
      const lang = Storage.getLanguage(this.state.currentLanguageId);
      const textarea = document.getElementById('editor-content-input');
      if (lang && textarea) {
        const btn = document.getElementById('btn-editor-speak');
        btn.classList.add('playing');
        Speech.speak(textarea.value, lang.name, () => {
          btn.classList.remove('playing');
        });
      }
    });

    // Controles de Flashcards
    document.getElementById('btn-flashcard-flip')?.addEventListener('click', () => this.flipFlashcard());
    document.getElementById('flashcard-card')?.addEventListener('click', () => this.flipFlashcard());
    document.getElementById('btn-flashcard-prev')?.addEventListener('click', () => this.prevFlashcard());
    document.getElementById('btn-flashcard-next')?.addEventListener('click', () => this.nextFlashcard());
    document.getElementById('btn-flashcard-shuffle')?.addEventListener('click', () => this.shuffleFlashcards());
    document.getElementById('btn-flashcard-exit')?.addEventListener('click', () => this.switchView('list'));

    // Atajos de teclado para Flashcards y Navegación
    window.addEventListener('keydown', (e) => {
      if (this.state.view === 'flashcards') {
        if (e.code === 'Space') {
          e.preventDefault();
          this.flipFlashcard();
        } else if (e.code === 'ArrowRight') {
          this.nextFlashcard();
        } else if (e.code === 'ArrowLeft') {
          this.prevFlashcard();
        } else if (e.code === 'Escape') {
          this.switchView('list');
        }
      }
    });

    // Cerrar modales con botones de cancelar o fondo
    document.querySelectorAll('.modal-close, .modal-backdrop').forEach(elem => {
      elem.addEventListener('click', (e) => {
        if (e.target === elem) {
          this.closeAllModals();
        }
      });
    });
  },

  // --- Manejo del Tema ---
  initTheme() {
    const saved = Storage.getTheme();
    document.documentElement.setAttribute('data-theme', saved);
    this.updateThemeIcon(saved);
  },

  toggleTheme() {
    const current = Storage.getTheme();
    const next = current === 'dark' ? 'light' : 'dark';
    Storage.setTheme(next);
    this.updateThemeIcon(next);
  },

  updateThemeIcon(theme) {
    const icon = document.getElementById('theme-icon');
    if (icon) {
      icon.innerHTML = theme === 'dark'
        ? `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`
        : `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`;
    }
  },

  // --- Cambio de Vistas ---
  switchView(viewName) {
    this.state.view = viewName;
    document.querySelectorAll('.view-section').forEach(sec => sec.classList.remove('active'));
    
    const target = document.getElementById(`view-${viewName}`);
    if (target) {
      target.classList.add('active');
      target.classList.add('fade-in');
    }
  },

  // --- Renderizado de Idiomas en Sidebar ---
  renderLanguages() {
    const listContainer = document.getElementById('language-list-container');
    if (!listContainer) return;

    const languages = Storage.getLanguages();
    listContainer.innerHTML = '';

    if (languages.length === 0) {
      listContainer.innerHTML = `
        <div style="padding: 18px 12px; text-align: center; color: var(--text-muted); font-size: 0.85rem;">
          <p>🌱 Sin idiomas aún</p>
          <button class="btn btn-primary btn-sm" id="btn-empty-add-lang" style="margin-top: 10px;">＋ Crear idioma</button>
        </div>
      `;
      document.getElementById('btn-empty-add-lang')?.addEventListener('click', () => this.openNewLanguageModal());
      return;
    }

    languages.forEach(lang => {
      const countTotal = (lang.entries.palabras?.length || 0) +
                         (lang.entries.frases?.length || 0) +
                         (lang.entries.textos?.length || 0);

      const item = document.createElement('div');
      item.className = `language-item ${lang.id === this.state.currentLanguageId ? 'active' : ''}`;
      item.innerHTML = `
        <div class="language-item-left">
          <span class="language-flag">${lang.flag || getFlag(lang.name)}</span>
          <span class="language-name">${lang.name}</span>
        </div>
        <span class="badge ${lang.id === this.state.currentLanguageId ? 'badge-primary' : ''}">${countTotal}</span>
      `;

      item.addEventListener('click', () => {
        this.selectLanguage(lang.id);
        // En móvil cerrar drawer
        document.getElementById('sidebar')?.classList.remove('open');
        document.getElementById('sidebar-overlay')?.classList.remove('open');
      });

      listContainer.appendChild(item);
    });
  },

  // --- Selección de Idioma ---
  selectLanguage(langId) {
    this.state.currentLanguageId = langId;
    this.renderLanguages();

    const lang = Storage.getLanguage(langId);
    if (!lang) {
      this.renderWelcome();
      return;
    }

    // Actualizar Hero Banner
    const heroFlag = document.getElementById('hero-language-flag');
    const heroTitle = document.getElementById('hero-language-title');
    const heroMeta = document.getElementById('hero-language-meta');

    if (heroFlag) heroFlag.textContent = lang.flag || getFlag(lang.name);
    if (heroTitle) heroTitle.textContent = lang.name;

    const wordsCount = lang.entries.palabras?.length || 0;
    const phrasesCount = lang.entries.frases?.length || 0;
    const textsCount = lang.entries.textos?.length || 0;

    if (heroMeta) {
      heroMeta.innerHTML = `
        <span>🌱 ${wordsCount} palabras</span> • 
        <span>🌿 ${phrasesCount} frases</span> • 
        <span>📜 ${textsCount} textos</span>
      `;
    }

    // Actualizar badges de tabs
    document.getElementById('tab-count-palabras').textContent = wordsCount;
    document.getElementById('tab-count-frases').textContent = phrasesCount;
    document.getElementById('tab-count-textos').textContent = textsCount;

    this.switchView('list');
    this.renderContentList();
  },

  selectCategory(category) {
    this.state.currentCategory = category;
    document.querySelectorAll('.category-tab').forEach(t => {
      t.classList.toggle('active', t.dataset.category === category);
    });

    // Actualizar texto del botón de crear en la barra de tabs
    const btnText = document.getElementById('btn-new-entry-tab-text');
    if (btnText) {
      const labels = { palabras: 'palabra', frases: 'frase', textos: 'texto' };
      btnText.textContent = `＋ Nueva ${labels[category] || 'entrada'}`;
    }

    this.renderContentList();
  },

  // --- Renderizado de Lista de Entradas ---
  renderContentList() {
    const container = document.getElementById('content-grid-container');
    const emptyState = document.getElementById('empty-category-state');
    if (!container) return;

    const lang = Storage.getLanguage(this.state.currentLanguageId);
    if (!lang) return;

    let entries = lang.entries[this.state.currentCategory] || [];

    // Filtrar por búsqueda si hay query
    if (this.state.searchQuery) {
      const q = this.state.searchQuery;
      entries = entries.filter(e => 
        (e.title && e.title.toLowerCase().includes(q)) ||
        (e.body && e.body.toLowerCase().includes(q))
      );
    }

    container.innerHTML = '';

    if (entries.length === 0) {
      container.style.display = 'none';
      if (emptyState) {
        emptyState.style.display = 'block';
        const titles = {
          palabras: 'No hay palabras registradas todavía',
          frases: 'No hay frases registradas todavía',
          textos: 'No hay textos registrados todavía'
        };
        document.getElementById('empty-state-title').textContent = this.state.searchQuery 
          ? 'No se encontraron resultados' 
          : (titles[this.state.currentCategory] || 'Sin contenido');
      }
      return;
    }

    if (emptyState) emptyState.style.display = 'none';
    container.style.display = 'grid';

    entries.forEach(entry => {
      const card = document.createElement('div');
      card.className = 'content-card fade-in';

      // Extraer primera línea descriptiva o resumen sin encabezados
      const cleanBody = entry.body
        .replace(/^#+\s+.+$/gm, '')
        .replace(/\*\*/g, '')
        .trim();
      const previewText = cleanBody || entry.title;

      card.innerHTML = `
        <div class="content-card-header">
          <h3 class="content-card-title">${entry.title}</h3>
          <button class="btn-speech" title="Escuchar pronunciación" data-speak-text="${encodeURIComponent(entry.title)}">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
          </button>
        </div>
        <p class="content-card-preview">${previewText}</p>
        <div class="content-card-footer">
          <span>${new Date(entry.updatedAt || entry.createdAt).toLocaleDateString()}</span>
          <div class="card-actions">
            <button class="btn-icon btn-sm btn-card-download" title="Descargar Markdown">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            </button>
            <button class="btn-icon btn-sm btn-card-delete" title="Eliminar entrada" style="color: var(--status-error);">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
            </button>
          </div>
        </div>
      `;

      // Evento clic en la tarjeta -> abrir editor
      card.addEventListener('click', (e) => {
        // Evitar abrir si hizo clic en un botón interno
        if (e.target.closest('button')) return;
        this.openEditor(entry.id);
      });

      // Botón de audio
      const speechBtn = card.querySelector('.btn-speech');
      speechBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        speechBtn.classList.add('playing');
        Speech.speak(entry.title, lang.name, () => {
          speechBtn.classList.remove('playing');
        });
      });

      // Botón de descarga
      card.querySelector('.btn-card-download').addEventListener('click', (e) => {
        e.stopPropagation();
        Storage.downloadMarkdownFile(entry.slug || entry.title, entry.body);
        this.showToast('Descargado archivo .md', 'success');
      });

      // Botón de eliminar
      card.querySelector('.btn-card-delete').addEventListener('click', (e) => {
        e.stopPropagation();
        if (confirm(`¿Eliminar permanentemente "${entry.title}"?`)) {
          Storage.deleteEntry(this.state.currentLanguageId, this.state.currentCategory, entry.id);
          this.selectLanguage(this.state.currentLanguageId);
          this.showToast('Entrada eliminada', 'info');
        }
      });

      container.appendChild(card);
    });
  },

  // --- Editor Markdown ---
  openEditor(entryId) {
    this.state.currentEntryId = entryId;
    const entry = this.getCurrentEntry();
    if (!entry) return;

    const lang = Storage.getLanguage(this.state.currentLanguageId);

    // Breadcrumb
    const bcLang = document.getElementById('editor-bc-lang');
    const bcCat = document.getElementById('editor-bc-cat');
    if (bcLang) bcLang.textContent = lang.name;
    if (bcCat) bcCat.textContent = this.state.currentCategory;

    // Título
    const titleInput = document.getElementById('editor-title-input');
    if (titleInput) titleInput.value = entry.title;

    // Contenido
    const textarea = document.getElementById('editor-content-input');
    if (textarea) textarea.value = entry.body;

    // Vista previa inicial
    this.updateLivePreview();
    this.updateStats();

    this.switchView('editor');
  },

  getCurrentEntry() {
    const lang = Storage.getLanguage(this.state.currentLanguageId);
    if (!lang) return null;
    const list = lang.entries[this.state.currentCategory] || [];
    return list.find(e => e.id === this.state.currentEntryId) || null;
  },

  handleEditorChange() {
    this.updateLivePreview();
    this.updateStats();

    // Auto-guardado con debounce de 600ms
    clearTimeout(this.state.autoSaveTimeout);
    this.state.autoSaveTimeout = setTimeout(() => {
      this.saveCurrentEditorEntry(true);
    }, 600);
  },

  updateLivePreview() {
    const textarea = document.getElementById('editor-content-input');
    const preview = document.getElementById('editor-preview-content');
    if (textarea && preview) {
      preview.innerHTML = Markdown.render(textarea.value);
    }
  },

  updateStats() {
    const textarea = document.getElementById('editor-content-input');
    if (!textarea) return;
    const text = textarea.value.trim();
    const words = text ? text.split(/\s+/).length : 0;
    const chars = text.length;

    const statsElem = document.getElementById('editor-stats');
    if (statsElem) {
      statsElem.textContent = `${words} palabras • ${chars} caracteres`;
    }
  },

  setEditorViewMode(mode) {
    this.state.editorMode = mode;
    const splitContainer = document.getElementById('editor-split-container');
    if (!splitContainer) return;

    splitContainer.className = `editor-split-view ${mode === 'edit' ? 'edit-only' : mode === 'preview' ? 'preview-only' : ''}`;
    
    document.querySelectorAll('.editor-view-toggle').forEach(b => {
      b.classList.toggle('active', b.dataset.mode === mode);
    });
  },

  saveCurrentEditorEntry(isAuto = false) {
    if (!this.state.currentEntryId || !this.state.currentLanguageId) return;

    const textarea = document.getElementById('editor-content-input');
    const titleInput = document.getElementById('editor-title-input');
    if (!textarea) return;

    const newBody = textarea.value;
    const customTitle = titleInput ? titleInput.value.trim() : null;

    try {
      Storage.updateEntry(
        this.state.currentLanguageId,
        this.state.currentCategory,
        this.state.currentEntryId,
        newBody,
        customTitle
      );

      const statusElem = document.getElementById('editor-save-status');
      if (statusElem) {
        statusElem.textContent = '✓ Guardado';
        statusElem.style.color = 'var(--status-success)';
      }

      if (!isAuto) {
        this.showToast('Cambios guardados correctamente', 'success');
      }
    } catch (e) {
      console.error(e);
      if (!isAuto) this.showToast('Error al guardar', 'error');
    }
  },

  // --- Flashcards / Modo Práctica ---
  startPracticeMode() {
    const lang = Storage.getLanguage(this.state.currentLanguageId);
    if (!lang) return;

    // Unir palabras y frases para el repaso
    const words = (lang.entries.palabras || []).map(w => ({ ...w, type: 'Palabra' }));
    const phrases = (lang.entries.frases || []).map(p => ({ ...p, type: 'Frase' }));
    const allItems = [...words, ...phrases];

    if (allItems.length === 0) {
      this.showToast('Agrega al menos una palabra o frase para practicar.', 'warning');
      return;
    }

    this.state.flashcardList = allItems;
    this.state.flashcardIndex = 0;

    const practiceLangName = document.getElementById('practice-language-name');
    if (practiceLangName) practiceLangName.textContent = lang.name;

    this.renderCurrentFlashcard();
    this.switchView('flashcards');
  },

  renderCurrentFlashcard() {
    const list = this.state.flashcardList;
    if (list.length === 0) return;

    const current = list[this.state.flashcardIndex];
    const card = document.getElementById('flashcard-card');
    if (card) card.classList.remove('flipped');

    // Frente
    document.getElementById('flashcard-type-label').textContent = current.type;
    document.getElementById('flashcard-front-title').textContent = current.title;

    // Reverso (definición o notas sin encabezado inicial)
    const cleanBack = current.body.replace(/^#+\s+.+$/gm, '').trim();
    document.getElementById('flashcard-back-content').innerHTML = Markdown.render(cleanBack || current.title);

    // Contador y Barra de Progreso
    const counter = document.getElementById('flashcard-counter-label');
    if (counter) {
      counter.textContent = `${this.state.flashcardIndex + 1} / ${list.length}`;
    }

    const progressFill = document.getElementById('flashcard-progress');
    if (progressFill) {
      const pct = ((this.state.flashcardIndex + 1) / list.length) * 100;
      progressFill.style.width = `${pct}%`;
    }
  },

  flipFlashcard() {
    const card = document.getElementById('flashcard-card');
    if (card) card.classList.toggle('flipped');
  },

  nextFlashcard() {
    if (this.state.flashcardIndex < this.state.flashcardList.length - 1) {
      this.state.flashcardIndex++;
      this.renderCurrentFlashcard();
    } else {
      this.showToast('¡Has completado todas las tarjetas!', 'success');
    }
  },

  prevFlashcard() {
    if (this.state.flashcardIndex > 0) {
      this.state.flashcardIndex--;
      this.renderCurrentFlashcard();
    }
  },

  shuffleFlashcards() {
    for (let i = this.state.flashcardList.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [this.state.flashcardList[i], this.state.flashcardList[j]] = [this.state.flashcardList[j], this.state.flashcardList[i]];
    }
    this.state.flashcardIndex = 0;
    this.renderCurrentFlashcard();
    this.showToast('Tarjetas mezcladas 🔀', 'info');
  },

  // --- Modales ---
  openModal(modalId) {
    this.closeAllModals();
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.classList.add('active');
      const firstInput = modal.querySelector('input, select, textarea');
      if (firstInput) setTimeout(() => firstInput.focus(), 100);
    }
  },

  closeAllModals() {
    document.querySelectorAll('.modal-backdrop').forEach(m => m.classList.remove('active'));
  },

  openNewLanguageModal() {
    const nameInput = document.getElementById('modal-lang-name');
    if (nameInput) nameInput.value = '';

    // Generar selector de banderas
    const flagGrid = document.getElementById('modal-flag-picker');
    let selectedFlag = '📚';

    if (flagGrid) {
      flagGrid.innerHTML = '';
      const flags = Object.values(LANGUAGE_FLAGS);
      const uniqueFlags = [...new Set(flags)];

      uniqueFlags.forEach(f => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = `flag-opt-btn ${f === selectedFlag ? 'selected' : ''}`;
        btn.textContent = f;
        btn.addEventListener('click', () => {
          flagGrid.querySelectorAll('.flag-opt-btn').forEach(b => b.classList.remove('selected'));
          btn.classList.add('selected');
          selectedFlag = f;
        });
        flagGrid.appendChild(btn);
      });
    }

    const form = document.getElementById('form-new-language');
    if (form) {
      form.onsubmit = (e) => {
        e.preventDefault();
        const name = nameInput.value.trim();
        if (!name) return;
        try {
          const newLang = Storage.createLanguage(name, selectedFlag);
          this.closeAllModals();
          this.selectLanguage(newLang.id);
          this.showToast(`Idioma "${name}" creado`, 'success');
        } catch (err) {
          this.showToast(err.message, 'error');
        }
      };
    }

    this.openModal('modal-new-language');
  },

  openNewEntryModal() {
    const lang = Storage.getLanguage(this.state.currentLanguageId);
    if (!lang) {
      this.showToast('Primero crea o selecciona un idioma.', 'warning');
      return;
    }

    // Modal dinámico según categoría
    const cat = this.state.currentCategory;
    const titleInput = document.getElementById('modal-entry-title');
    const bodyInput = document.getElementById('modal-entry-body');
    const labelTitle = document.getElementById('modal-entry-title-label');
    const groupBody = document.getElementById('modal-entry-body-group');
    const modalTitle = document.getElementById('modal-new-entry-header');

    if (titleInput) titleInput.value = '';
    if (bodyInput) bodyInput.value = '';

    if (cat === 'palabras') {
      modalTitle.textContent = `Nueva Palabra para ${lang.name}`;
      labelTitle.textContent = 'Palabra:';
      titleInput.placeholder = 'Ej: Perspicaz, Saudade, Serendipia...';
      groupBody.style.display = 'flex';
      bodyInput.placeholder = 'Definición, etimología o ejemplo...';
    } else if (cat === 'frases') {
      modalTitle.textContent = `Nueva Frase para ${lang.name}`;
      labelTitle.textContent = 'Frase:';
      titleInput.placeholder = 'Ej: In bocca al lupo, Once in a blue moon...';
      groupBody.style.display = 'flex';
      bodyInput.placeholder = 'Significado, contexto de uso...';
    } else {
      modalTitle.textContent = `Nuevo Texto para ${lang.name}`;
      labelTitle.textContent = 'Título del texto:';
      titleInput.placeholder = 'Ej: Notas de gramática, Cuento corto...';
      groupBody.style.display = 'flex';
      bodyInput.placeholder = 'Contenido del texto en Markdown...';
    }

    const form = document.getElementById('form-new-entry');
    if (form) {
      form.onsubmit = (e) => {
        e.preventDefault();
        const title = titleInput.value.trim();
        const body = bodyInput.value.trim();
        if (!title) return;

        try {
          const entry = Storage.createEntry(lang.id, cat, title, body);
          this.closeAllModals();
          this.selectLanguage(lang.id);
          this.showToast(`Guardado en ${cat}`, 'success');
          // Abrir editor directamente para seguir completando
          this.openEditor(entry.id);
        } catch (err) {
          this.showToast(err.message, 'error');
        }
      };
    }

    this.openModal('modal-new-entry');
  },

  openImportModal() {
    const fileInput = document.getElementById('modal-import-file');
    if (fileInput) fileInput.value = '';

    const form = document.getElementById('form-import-backup');
    if (form) {
      form.onsubmit = (e) => {
        e.preventDefault();
        const file = fileInput.files[0];
        if (!file) {
          this.showToast('Selecciona un archivo JSON válido.', 'warning');
          return;
        }

        const reader = new FileReader();
        reader.onload = (event) => {
          try {
            Storage.importJSON(event.target.result);
            this.closeAllModals();
            this.renderLanguages();
            const langs = Storage.getLanguages();
            if (langs.length > 0) this.selectLanguage(langs[0].id);
            this.showToast('¡Copia de respaldo restaurada con éxito!', 'success');
          } catch (err) {
            this.showToast(err.message, 'error');
          }
        };
        reader.readAsText(file);
      };
    }

    this.openModal('modal-import');
  },

  renderWelcome() {
    this.switchView('list');
    const heroTitle = document.getElementById('hero-language-title');
    if (heroTitle) heroTitle.textContent = 'Bienvenido a Language Library';
  },

  // --- Notificaciones Toast ---
  showToast(message, type = 'info') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;

    const icons = {
      success: '🌿',
      error: '⚠️',
      warning: '🍂',
      info: '🌱'
    };

    toast.innerHTML = `
      <span>${icons[type] || '🌱'}</span>
      <span>${message}</span>
    `;

    container.appendChild(toast);

    setTimeout(() => {
      toast.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
      toast.style.opacity = '0';
      toast.style.transform = 'translateX(100%)';
      setTimeout(() => toast.remove(), 300);
    }, 3200);
  }
};
