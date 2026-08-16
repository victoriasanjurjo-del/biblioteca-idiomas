/**
 * markdown.js — Parser y Renderizador de Markdown ligero y seguro
 * Soporta títulos, listas, citas, negritas, cursivas, código y bloques.
 */

export const Markdown = {
  /**
   * Convierte texto Markdown en HTML sanitizado
   * @param {string} md - Texto en formato Markdown
   * @returns {string} HTML renderizado
   */
  render(md) {
    if (!md) return '';

    // Escapar etiquetas HTML básicas para evitar XSS
    let html = md
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

    // Bloques de código ```lang ... ```
    html = html.replace(/```([a-zA-Z0-9_-]*)\n([\s\S]*?)```/g, (match, lang, code) => {
      return `<pre><code class="language-${lang || 'text'}">${code.trim()}</code></pre>`;
    });

    // Código en línea `code`
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Títulos (# H1, ## H2, ### H3, #### H4)
    html = html.replace(/^#### (.*$)/gim, '<h4>$1</h4>');
    html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
    html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
    html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');

    // Regla horizontal ---
    html = html.replace(/^---$/gim, '<hr style="border:0;border-top:1px solid var(--border-subtle);margin:20px 0;">');

    // Blockquotes > texto
    html = html.replace(/^\> (.*$)/gim, '<blockquote>$1</blockquote>');

    // Negrita y Cursiva
    html = html.replace(/\*\*\*(.*?)\*\*\*/g, '<strong><em>$1</em></strong>');
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');
    html = html.replace(/___(.*?)___/g, '<strong><em>$1</em></strong>');
    html = html.replace(/__(.*?)__/g, '<strong>$1</strong>');
    html = html.replace(/_(.*?)_/g, '<em>$1</em>');

    // Tachado ~~texto~~
    html = html.replace(/~~(.*?)~~/g, '<del>$1</del>');

    // Listas no ordenadas (- item o * item)
    html = html.replace(/^\s*[\-\*]\s+(.*)$/gim, '<ul><li>$1</li></ul>');
    // Unir </ul><ul> contiguos
    html = html.replace(/<\/ul>\s?<ul>/g, '');

    // Listas ordenadas (1. item)
    html = html.replace(/^\s*\d+\.\s+(.*)$/gim, '<ol><li>$1</li></ol>');
    // Unir </ol><ol> contiguos
    html = html.replace(/<\/ol>\s?<ol>/g, '');

    // Párrafos (líneas con contenido que no sean bloques)
    const lines = html.split('\n');
    let inParagraph = false;
    const processedLines = [];

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();

      if (!line) {
        if (inParagraph) {
          processedLines.push('</p>');
          inParagraph = false;
        }
        continue;
      }

      const isBlock = line.startsWith('<h') ||
                      line.startsWith('<ul') ||
                      line.startsWith('<ol') ||
                      line.startsWith('<li') ||
                      line.startsWith('<pre') ||
                      line.startsWith('<blockquote') ||
                      line.startsWith('<hr');

      if (isBlock) {
        if (inParagraph) {
          processedLines.push('</p>');
          inParagraph = false;
        }
        processedLines.push(line);
      } else {
        if (!inParagraph) {
          processedLines.push('<p>' + line);
          inParagraph = true;
        } else {
          processedLines.push('<br>' + line);
        }
      }
    }

    if (inParagraph) {
      processedLines.push('</p>');
    }

    return processedLines.join('\n');
  },

  /**
   * Inserta sintaxis markdown en una posición de textarea
   */
  insertFormatting(textarea, type) {
    const start = textarea.selectionStart;
    const end = textarea.selectionEnd;
    const text = textarea.value;
    const selected = text.substring(start, end);
    let replacement = '';
    let cursorOffset = 0;

    switch (type) {
      case 'bold':
        replacement = `**${selected || 'texto'}**`;
        cursorOffset = selected ? replacement.length : 2;
        break;
      case 'italic':
        replacement = `*${selected || 'texto'}*`;
        cursorOffset = selected ? replacement.length : 1;
        break;
      case 'h1':
        replacement = `\n# ${selected || 'Título'}\n`;
        cursorOffset = replacement.length;
        break;
      case 'h2':
        replacement = `\n## ${selected || 'Subtítulo'}\n`;
        cursorOffset = replacement.length;
        break;
      case 'quote':
        replacement = `\n> ${selected || 'Cita o nota reflexiva'}\n`;
        cursorOffset = replacement.length;
        break;
      case 'ul':
        replacement = `\n- ${selected || 'Elemento de lista'}\n`;
        cursorOffset = replacement.length;
        break;
      case 'code':
        replacement = selected.includes('\n')
          ? `\n\`\`\`\n${selected}\n\`\`\`\n`
          : `\`${selected || 'código'}\``;
        cursorOffset = replacement.length;
        break;
      default:
        return;
    }

    textarea.value = text.substring(0, start) + replacement + text.substring(end);
    textarea.focus();
    textarea.setSelectionRange(start + cursorOffset, start + cursorOffset);
  }
};
