import {initThemeSwitch} from "./themes.js";
const preloaderElement = document.querySelector('#preloader')
export const initListeners = () => {

    addEventListener('DOMContentLoaded', () => {
        setTimeout(() => {preloaderElement.toggleAttribute('hide')} ,500)

        setTimeout( () => {preloaderElement.remove()}, 1000)
    })
}