const state = {
  pageContext: {},
  viewingPlatform: {},
  currentImage: {},
  currentIndex: -1,
  fullScreenExpanded: false,
  newContentOptionsExpanded: false,
};

function registerFullPageContext(payload) {
  state.pageContext = payload;
  console.log(state);
}

function handleImageClick(url) {
  updatePageState(url);
  toggleFullScreen();
  generateFullScreenElements(url);
}

function handleImageKeyboardEvent(event) {
  let validCodes = ["Enter", "Space"];
  if (validCodes.includes(event.code)) {
    handleImageClick(event.target.getAttribute("data-url"));
    event.preventDefault();
    event.stopPropagation();
  }
}

const toggleNewContentOptions = () => {
  const options = document.getElementById(CONSTANTS.newContentOptionsId);
  if (Array.from(options.classList)?.includes("hidden")) {
    flipClasses("hidden", "flex", options);
    state.newContentOptionsExpanded = true;
  } else {
    flipClasses("flex", "hidden", options);
    state.newContentOptionsExpanded = false;
  }
};

const toggleFullScreen = () => {
  const targetDiv =
    state.viewingPlatform == CONSTANTS.mobile
      ? CONSTANTS.mobileFullScreenId
      : CONSTANTS.desktopFullScreenId;
  console.log(targetDiv);
  const fullScreenDiv = document.getElementById(targetDiv);

  if (Array.from(fullScreenDiv.classList)?.includes("hidden")) {
    flipClasses("hidden", "flex", fullScreenDiv);
    state.fullScreenExpanded = true;
  } else {
    flipClasses("flex", "hidden", fullScreenDiv);
    state.fullScreenExpanded = false;
  }
};

const flipClasses = (fromClass, toClass, element) => {
  element.classList.remove(fromClass);
  element.classList.add(toClass);
};

const nextImage = () => {
  if (state.currentIndex == state.pageContext.pageArray.length - 1) {
    return;
  }

  state.currentIndex++;
  state.currentImage = state.pageContext.pageArray[state.currentIndex];
  generateDesktopFullScreenElements();
};

const lastImage = () => {
  if (state.currentIndex == 0) {
    return;
  }

  state.currentIndex--;
  state.currentImage = state.pageContext.pageArray[state.currentIndex];
  generateDesktopFullScreenElements();
};

const generateFullScreenElements = (url) => {
  if (state.viewingPlatform == CONSTANTS.mobile) {
    const target = generateMobileFullScreenElements(url);
    document.getElementById(target).scrollIntoView();
  } else {
    generateDesktopFullScreenElements();
    window.scrollTo(0, 0);
  }
};

const generateDesktopFullScreenElements = () => {
  const imagePanel = document.getElementById("expanded-image");

  imagePanel.src = state.currentImage.url;
  imagePanel.alt = state.currentImage.alt;
};

const generateMobileFullScreenElements = (targetUrl) => {
  console.log(targetUrl);
  const cont = document.getElementById("image-scroll-container");
  let targetId;
  state.pageContext.pageArray.forEach((element) => {
    const target = crypto.randomUUID();
    const newImage = CONSTANTS.imageTemplate
      .replace("{IMAGE_ID}", target)
      .replace("{IMG_SRC}", element.url)
      .replace("{ALT_TEXT}", element.alt);
    cont.innerHTML += newImage;
    if (targetUrl == element.url) {
      targetId = target;
    }
  });

  return targetId;
};

const updatePageState = (url) => {
  state.currentIndex = getIndexOfImageInPageComic(url);
  state.currentImage = state.pageContext.pageArray[state.currentIndex];
  state.viewingPlatform = getViewingPlatform();
  console.log(state);
};

const getIndexOfImageInPageComic = (url) => {
  return state.pageContext.pageArray
    .map(function (e) {
      return e.url;
    })
    .indexOf(url);
};

const getViewingPlatform = () => {
  const pageWidth = window
    .getComputedStyle(document.body)
    .getPropertyValue("width");
  console.log(pageWidth);
  if (!pageWidth) {
    return CONSTANTS.mobile;
  }

  console.log("nah ah ah");

  return parseFloat(pageWidth) >= CONSTANTS.mobileBreakPoint
    ? CONSTANTS.desktop
    : CONSTANTS.mobile;
};

const CONSTANTS = {
  mobile: "mobile",
  desktop: "desktop",
  mobileFullScreenId: "mobile-full-screen",
  desktopFullScreenId: "desktop-full-screen",
  newContentOptionsId: "new-content-options",
  mobileBreakPoint: 768,
  imageTemplate: `<img id="{IMAGE_ID}" class="relative mx-auto h-screen border-2 border-slate-100" src='{IMG_SRC}' alt='{ALT_TEXT}'/>`,
};

document.addEventListener("keydown", (event) => {
  let arrowKeys = ["ArrowRight", "ArrowLeft", "Escape"];
  if (
    arrowKeys.includes(event.key) &&
    state.fullScreenExpanded &&
    state.viewingPlatform == CONSTANTS.desktop
  ) {
    switch (event.key) {
      case "ArrowRight":
        nextImage();
        break;
      case "ArrowLeft":
        lastImage();
        break;
      case "Escape":
        if (state.fullScreenExpanded) {
          toggleFullScreen();
        } else if (state.newContentOptionsExpanded) {
          toggleNewContentOptions();
        }
        break;
      default:
        nextImage();
        break;
    }
  }
});
