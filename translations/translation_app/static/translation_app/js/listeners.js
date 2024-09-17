import {initThemeSwitch} from "./themes.js";
const preloaderElement = document.querySelector('#preloader')
export const initListeners = () => {

    addEventListener('DOMContentLoaded', () => {
        setTimeout(() => {preloaderElement.toggleAttribute('hide')} ,500)

        setTimeout( () => {preloaderElement.remove()}, 1000)
    })

    const videoplayer = document.getElementById('translationCardVideoplayer')
    if (videoplayer) {
        function requestFullScreen(element) {
            if (element.requestFullscreen) {
                element.requestFullscreen();
            } else if (element.mozRequestFullScreen) { // Firefox
                element.mozRequestFullScreen();
            } else if (element.webkitRequestFullscreen) { // Chrome, Safari, Opera
                element.webkitRequestFullscreen();
            } else if (element.msRequestFullscreen) { // IE/Edge
                element.msRequestFullscreen();
            }
        }
        videoplayer.addEventListener('click', () => {
            requestFullScreen(videoplayer)
        })
        window.addEventListener('orientationchange', (e) => {
            if (screen.orientation.angle === 90 || screen.orientation.angle === -90) {
                requestFullScreen(videoplayer)
            }
        })
    }


}