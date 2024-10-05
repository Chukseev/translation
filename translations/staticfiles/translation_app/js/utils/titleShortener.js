export const initTitleShortener = (titleElements) => {
    const TITLE_CHAR_COUNT = 40;

    titleElements.forEach((title) => {
        title.textContent = title.textContent.trim()
        if (title.textContent.length > TITLE_CHAR_COUNT ) {
            title.textContent = title.textContent.slice(0, TITLE_CHAR_COUNT) + '...'
        }
    })
}