/**
 * storage.js — Gestión de datos y persistencia en LocalStorage
 * Compatible con la estructura de carpetas Markdown y exportable.
 */

const STORAGE_KEY = 'language_library_data_v1';
const THEME_KEY = 'language_library_theme';

// Mapeo por defecto de nombres de idioma a emojis de bandera
export const LANGUAGE_FLAGS = {
  "Español": "🇪🇸",
  "English": "🇬🇧",
  "Italiano": "🇮🇹",
  "Deutsch": "🇩🇪",
  "Français": "🇫🇷",
  "Português": "🇵🇹",
  "日本語": "🇯🇵",
  "中文": "🇨🇳",
  "한국어": "🇰🇷",
  "Русский": "🇷🇺",
  "العربية": "🇸🇦",
  "Ελληνικά": "🇬🇷",
  "Nederlands": "🇳🇱",
  "Svenska": "🇸🇪",
  "Norsk": "🇳🇴",
  "Dansk": "🇩🇰",
  "Suomi": "🇫🇮",
  "Polski": "🇵🇱",
  "Čeština": "🇨🇿",
  "Türkçe": "🇹🇷",
  "हिन्दी": "🇮🇳",
  "Català": "🔶",
  "Euskara": "🔶",
  "Galego": "🔶",
};

export const DEFAULT_FLAG = "📚";

// Datos iniciales de demostración con estética botánica y contenido rico
const INITIAL_DATA = {
  languages: [
    {
      id: "espanol",
      name: "Español",
      flag: "🇪🇸",
      createdAt: new Date().toISOString(),
      entries: {
        palabras: [
          {
            id: "w-1",
            title: "perspicaz",
            slug: "perspicaz",
            body: "# perspicaz\n\n*adjetivo*\n\n1. Que es capaz de percatarse de cosas que pasan inadvertidas para los demás.\n2. Agudo y claro en el entendimiento.\n\n> *Ejemplo:* Su perspicaz mirada notó de inmediato la sutileza en el texto.",
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
          },
          {
            id: "w-2",
            title: "efímero",
            slug: "efimero",
            body: "# efímero\n\n*adjetivo*\n\nQue tiene una duración muy corta, pasajero.\n\n> *Ejemplo:* La floración primaveral del cerezo es tan hermosa como efímera.",
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
          },
          {
            id: "w-3",
            title: "serendipia",
            slug: "serendipia",
            body: "# serendipia\n\n*sustantivo femenino*\n\nDescubrimiento o hallazgo afortunado e inesperado que se produce cuando se está buscando otra cosa distinta.",
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
          }
        ],
        frases: [
          {
            id: "p-1",
            title: "A quien madruga, Dios le ayuda",
            slug: "a-quien-madruga-dios-le-ayuda",
            body: "# A quien madruga, Dios le ayuda\n\nRefrán popular que pondera la importancia de ser diligente y esforzado en el trabajo para lograr el éxito.",
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
          },
          {
            id: "p-2",
            title: "No hay mal que por bien no venga",
            slug: "no-hay-mal-que-por-bien-no-venga",
            body: "# No hay mal que por bien no venga\n\nExpresión que transmite optimismo, sugiriendo que de cualquier situación adversa puede surgir algo positivo.",
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
          }
        ],
        textos: [
          {
            id: "t-1",
            title: "El Jardín de los Senderos que se Bifurcan",
            slug: "el-jardin-de-los-senderos-que-se-bifurcan",
            body: "# El Jardín de los Senderos que se Bifurcan\n\n*Fragmento reflexivo de Jorge Luis Borges*\n\nEl tiempo se bifurca perpetuamente hacia innumerables futuros. En uno de ellos soy su enemigo; en otro, su amigo.\n\n---\n\n### Notas Lingüísticas\n- **Bifurcar:** Dividirse en dos ramales o caminos.\n- **Perpetuamente:** De manera continua e incesante.",
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
          }
        ]
      }
    },
    {
      id: "english",
      name: "English",
      flag: "🇬🇧",
      createdAt: new Date().toISOString(),
      entries: {
        palabras: [
          {
            id: "en-w-1",
            title: "Wanderlust",
            slug: "wanderlust",
            body: "# Wanderlust\n\n*noun* | /ˈwɒn.də.lʌst/\n\nA strong, innate desire or impulse to rove or travel and explore the world.\n\n> *Example:* Her wanderlust led her to backpack across South America.",
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
          },
          {
            id: "en-w-2",
            title: "Petrichor",
            slug: "petrichor",
            body: "# Petrichor\n\n*noun* | /ˈpet.rɪ.kɔːr/\n\nA pleasant smell that frequently accompanies the first rain after a long period of warm, dry weather.\n\n> *Notes:* Derived from Greek *petra* (stone) + *ichor* (the fluid in the veins of the gods).",
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
          }
        ],
        frases: [
          {
            id: "en-p-1",
            title: "Once in a blue moon",
            slug: "once-in-a-blue-moon",
            body: "# Once in a blue moon\n\n*idiom*\n\nMeaning: An event that happens very rarely.\n\n> *Example:* I only eat junk food once in a blue moon.",
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
          }
        ],
        textos: [
          {
            id: "en-t-1",
            title: "Walden: Life in the Woods",
            slug: "walden-life-in-the-woods",
            body: "# Walden: Life in the Woods\n\n*Henry David Thoreau (1854)*\n\n> \"I went to the woods because I wished to live deliberately, to front only the essential facts of life, and see if I could not learn what it had to teach.\"\n\n### Vocabulary Highlights\n- **Deliberately:** With intention and mindfulness.\n- **Front:** To confront or face directly.",
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
          }
        ]
      }
    },
    {
      id: "italiano",
      name: "Italiano",
      flag: "🇮🇹",
      createdAt: new Date().toISOString(),
      entries: {
        palabras: [
          {
            id: "it-w-1",
            title: "Apericena",
            slug: "apericena",
            body: "# Apericena\n\n*sostantivo maschile*\n\nUnione di *aperitivo* e *cena*. Un aperitivo ricco e abbondante che sostituisce la cena.",
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
          }
        ],
        frases: [
          {
            id: "it-p-1",
            title: "In bocca al lupo!",
            slug: "in-bocca-al-lupo",
            body: "# In bocca al lupo!\n\n*Modo di dire*\n\nAugurio di buona fortuna. La risposta corretta e tradizionale è **\"Crepi il lupo!\"** oppure **\"Viva il lupo!\"**.",
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
          }
        ],
        textos: []
      }
    }
  ]
};

export function getFlag(languageName) {
  if (LANGUAGE_FLAGS[languageName]) return LANGUAGE_FLAGS[languageName];
  const lower = languageName.toLowerCase();
  for (const [key, flag] of Object.entries(LANGUAGE_FLAGS)) {
    if (key.toLowerCase() === lower) return flag;
  }
  return DEFAULT_FLAG;
}

export function makeSlug(text) {
  return text
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)+/g, '') || 'item';
}

export const Storage = {
  getData() {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (!stored) {
        this.saveData(INITIAL_DATA);
        return INITIAL_DATA;
      }
      return JSON.parse(stored);
    } catch (e) {
      console.error('Error reading storage:', e);
      return INITIAL_DATA;
    }
  },

  saveData(data) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    } catch (e) {
      console.error('Error writing storage:', e);
    }
  },

  getLanguages() {
    const data = this.getData();
    return data.languages || [];
  },

  getLanguage(id) {
    const data = this.getData();
    return data.languages.find(l => l.id === id) || null;
  },

  createLanguage(name, flag = null) {
    const data = this.getData();
    const cleanName = name.trim();
    if (!cleanName) throw new Error('El nombre del idioma no puede estar vacío.');

    const id = makeSlug(cleanName);
    if (data.languages.some(l => l.id === id)) {
      throw new Error(`El idioma "${cleanName}" ya existe.`);
    }

    const newLang = {
      id,
      name: cleanName,
      flag: flag || getFlag(cleanName),
      createdAt: new Date().toISOString(),
      entries: {
        palabras: [],
        frases: [],
        textos: []
      }
    };

    data.languages.push(newLang);
    this.saveData(data);
    return newLang;
  },

  deleteLanguage(id) {
    const data = this.getData();
    data.languages = data.languages.filter(l => l.id !== id);
    this.saveData(data);
    return true;
  },

  createEntry(languageId, category, title, body = '') {
    const data = this.getData();
    const lang = data.languages.find(l => l.id === languageId);
    if (!lang) throw new Error('Idioma no encontrado.');

    if (!lang.entries[category]) {
      lang.entries[category] = [];
    }

    const cleanTitle = title.trim();
    if (!cleanTitle) throw new Error('El título no puede estar vacío.');

    const slug = makeSlug(cleanTitle);
    const id = `${category.slice(0, 1)}-${Date.now()}-${Math.random().toString(36).substr(2, 4)}`;

    // Si el body está vacío, armamos el contenido Markdown base
    const content = body.trim() ? body : `# ${cleanTitle}\n\n${cleanTitle}\n`;

    const newEntry = {
      id,
      title: cleanTitle,
      slug,
      body: content,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    };

    lang.entries[category].unshift(newEntry);
    this.saveData(data);
    return newEntry;
  },

  updateEntry(languageId, category, entryId, newBody, newTitle = null) {
    const data = this.getData();
    const lang = data.languages.find(l => l.id === languageId);
    if (!lang || !lang.entries[category]) throw new Error('Entrada no encontrada.');

    const entry = lang.entries[category].find(e => e.id === entryId);
    if (!entry) throw new Error('Entrada no encontrada.');

    entry.body = newBody;
    entry.updatedAt = new Date().toISOString();

    // Extraer título si empieza con # en markdown
    if (newTitle) {
      entry.title = newTitle;
    } else {
      const match = newBody.match(/^#\s+(.+)$/m);
      if (match) {
        entry.title = match[1].trim();
      }
    }

    this.saveData(data);
    return entry;
  },

  deleteEntry(languageId, category, entryId) {
    const data = this.getData();
    const lang = data.languages.find(l => l.id === languageId);
    if (!lang || !lang.entries[category]) return false;

    lang.entries[category] = lang.entries[category].filter(e => e.id !== entryId);
    this.saveData(data);
    return true;
  },

  exportJSON() {
    const data = this.getData();
    const jsonString = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(data, null, 2));
    const downloadAnchor = document.createElement('a');
    downloadAnchor.setAttribute("href", jsonString);
    downloadAnchor.setAttribute("download", `biblioteca_idiomas_backup_${new Date().toISOString().slice(0, 10)}.json`);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
  },

  importJSON(jsonString) {
    try {
      const parsed = JSON.parse(jsonString);
      if (!parsed.languages || !Array.isArray(parsed.languages)) {
        throw new Error('Estructura de respaldo inválida.');
      }
      this.saveData(parsed);
      return true;
    } catch (e) {
      throw new Error('Error al importar archivo JSON: ' + e.message);
    }
  },

  downloadMarkdownFile(filename, content) {
    const blob = new Blob([content], { type: 'text/markdown;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename.endsWith('.md') ? filename : `${filename}.md`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  },

  // Tema
  getTheme() {
    return localStorage.getItem(THEME_KEY) || 'light';
  },

  setTheme(theme) {
    localStorage.setItem(THEME_KEY, theme);
    document.documentElement.setAttribute('data-theme', theme);
  }
};
