import {initTitleShortener} from "./utils/titleShortener.js";
import {initListeners} from './listeners.js';
import {initThemeSwitch} from "./themes.js";

const itemTitleElements = document.querySelectorAll('.translations__item-title')


initListeners();
initThemeSwitch();
initTitleShortener(itemTitleElements);