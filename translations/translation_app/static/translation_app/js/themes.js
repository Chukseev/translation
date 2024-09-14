var themeMode = null;
var htmlElement = document.querySelector('html')
let switchButtonElement = null;
const themeModeFromStorage = localStorage.getItem('themeMode')

const switchThemeMode = () => {
    if (themeMode === 'light')
        themeMode = 'dark';
    else
        themeMode = 'light';

    localStorage.setItem('themeMode', themeMode)
}

const createThemeSwitchButton = () => {
    document.body.insertAdjacentHTML("beforeend",
        `<button id="theme-switch" light></button>`)
    switchButtonElement = document.getElementById('theme-switch')
    switchButtonElement.addEventListener('click', onClickSwitchButton)
    updateSwitchButton();
}

const updateRootAttribute = () => {
    const dataTheme = htmlElement.getAttribute('data-theme')
    if (dataTheme === 'light')
        htmlElement.setAttribute('data-theme', 'dark')
    else
        htmlElement.setAttribute('data-theme', 'light')
}

const onClickSwitchButton = () => {
    switchThemeMode()
    updateRootAttribute()
    updateSwitchButton()
}

const updateSwitchButton = () => {
    if (themeMode === 'dark') {
        switchButtonElement.removeAttribute('light');
        switchButtonElement.setAttribute('dark', '')
    }

    else {
        switchButtonElement.removeAttribute('dark');
        switchButtonElement.setAttribute('light', '');

    }

}

const isPreferThemeDark = () => {
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
    if (prefersDarkScheme.matches) {
        return true
    }
    else {
        return false
    }
}


const initThemeMode = () => {
    if (themeModeFromStorage) {
        themeMode = themeModeFromStorage;
        updateRootAttribute();
        updateSwitchButton();
        console.log('themeMode в стораже существует')

    }
    else {
        if (isPreferThemeDark()) {
            themeMode = 'dark';
        }
        else {
            themeMode = 'light';
        }
    }

    htmlElement.setAttribute('data-theme', themeMode);
    console.log('themeFromStorage: ', themeModeFromStorage)

}








export const initThemeSwitch = () => {
    createThemeSwitchButton()
    initThemeMode()
}

