/**
 * speech.js — Reproducción de voz y pronunciación mediante Web Speech API
 */

const LANG_CODE_MAP = {
  "español": "es-ES",
  "spanish": "es-ES",
  "english": "en-US",
  "inglés": "en-US",
  "italiano": "it-IT",
  "italian": "it-IT",
  "deutsch": "de-DE",
  "alemán": "de-DE",
  "français": "fr-FR",
  "francés": "fr-FR",
  "português": "pt-PT",
  "portugués": "pt-PT",
  "日本語": "ja-JP",
  "japanese": "ja-JP",
  "中文": "zh-CN",
  "chinese": "zh-CN",
  "한국어": "ko-KR",
  "korean": "ko-KR",
  "русский": "ru-RU",
  "russian": "ru-RU",
  "عربية": "ar-SA",
  "arabic": "ar-SA",
  "ελληνικά": "el-GR",
  "greek": "el-GR",
  "nederlands": "nl-NL",
  "dutch": "nl-NL",
  "svenska": "sv-SE",
  "swedish": "sv-SE",
  "norsk": "no-NO",
  "norwegian": "no-NO",
  "dansk": "da-DK",
  "danish": "da-DK",
  "suomi": "fi-FI",
  "finnish": "fi-FI",
  "polski": "pl-PL",
  "polish": "pl-PL",
  "čeština": "cs-CZ",
  "czech": "cs-CZ",
  "türkçe": "tr-TR",
  "turkish": "tr-TR",
  "català": "ca-ES",
  "galego": "gl-ES",
  "euskara": "eu-ES"
};

export const Speech = {
  isSupported() {
    return 'speechSynthesis' in window && 'SpeechSynthesisUtterance' in window;
  },

  getLangCode(languageName) {
    if (!languageName) return 'es-ES';
    const key = languageName.toLowerCase().trim();
    return LANG_CODE_MAP[key] || 'es-ES';
  },

  speak(text, languageName, onEndCallback = null) {
    if (!this.isSupported()) {
      console.warn('SpeechSynthesis no es soportado por este navegador.');
      if (onEndCallback) onEndCallback();
      return;
    }

    // Limpiar síntesis anterior si está hablando
    window.speechSynthesis.cancel();

    // Limpiar sintaxis markdown del texto para lectura limpia
    const cleanText = text
      .replace(/^#+\s+/gm, '')
      .replace(/\*\*([^*]+)\*\*/g, '$1')
      .replace(/\*([^*]+)\*/g, '$1')
      .replace(/`([^`]+)`/g, '$1')
      .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
      .replace(/>/g, '')
      .trim();

    if (!cleanText) {
      if (onEndCallback) onEndCallback();
      return;
    }

    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.lang = this.getLangCode(languageName);
    utterance.rate = 0.92; // Ritmo natural y claro para aprendizaje
    utterance.pitch = 1.0;

    if (onEndCallback) {
      utterance.onend = onEndCallback;
      utterance.onerror = onEndCallback;
    }

    window.speechSynthesis.speak(utterance);
  },

  stop() {
    if (this.isSupported()) {
      window.speechSynthesis.cancel();
    }
  }
};
