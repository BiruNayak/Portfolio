import { generateServices, generatePortfolio } from './modules/contentRenderer.js';
import { handleFormSubmission } from './modules/formHandler.js';
import { opentab, openmenu, closemenu } from './main.js';

window.onload = () => {
  generateServices();
  generatePortfolio();
  handleFormSubmission();
};

// Attach tab/menu events globally
window.opentab = opentab;
window.openmenu = openmenu;
window.closemenu = closemenu;
