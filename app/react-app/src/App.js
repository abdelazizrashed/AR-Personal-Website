/* eslint-disable no-unused-vars */
import "./styles/App.css";
import { useState, useEffect } from "react";
//* Components import
import NavBar from "./components/partials/NavBar";
import Footer from "./components/partials/Footer";
import Home from "./components/pages/Home";
import About from "./components/pages/About";
import Projects from "./components/pages/Projects";
import Services from "./components/pages/Services";
import Certificates from "./components/pages/Certificates";
import Contact from "./components/pages/Contact";
import Resume from "./components/pages/Resume";
import Project from "./components/pages/Project";
import Service from "./components/pages/Service";
import Certificate from "./components/pages/Certificate";
import psPC from "./img/ps-pc.png";
import psIpad from "./img/ps-phone.png";

function App() {
  // UseState hook variables
  var imgsInfo;
  if (!window.info || window.info === "") {
    imgsInfo = {
      mac: {
        url: psPC,
        alt: "Abdelaziz Rashed Personal website screenshot in laptop resolution",
      },
      ipad: {
        url: psIpad,
        alt: "Abdelaziz Rashed Personal website screenshot in tablet resolution",
      },
      phone: {
        url: null,
        alt: "Abdelaziz Rashed Personal website screenshot in phone resolution",
      },
    };
  } else {
    imgsInfo = {
      mac: window.info.homeLaptopImgInfo,
      ipad: window.info.homeTabletImgInfo,
      phone: window.info.homePhoneImgInfo,
    };
  }
  const [websiteIMGs, setWebsiteIMGs] = useState(imgsInfo);

  var nav;
  if (!window.navItems || window.navItems === "") {
    nav = [
      {
        name: "Home",
        url: "/",
      },
      {
        name: "Projects",
        url: "/projects",
      },
      {
        name: "Services",
        url: "/services",
      },
      {
        name: "Contact",
        url: "/contact",
      },
      {
        name: "Resume",
        url: "/resume",
      },
      {
        name: "Certificates",
        url: "/certificates",
      },
      {
        name: "About",
        url: "/about",
      },
    ];
  } else {
    nav = window.navItems;
  }
  const [navItems, setNavItems] = useState(nav);

  const [homeIntro, setHomeIntro] = useState(
    "Freelance Software Developer from Egypt. \nHighly experienced in Full-Stack Web Development, Game Development, and Cross-Platform App Development."
  );

  const [fillerStyle, setFillerStyle] = useState({});

  //Function variables
  useEffect(() => {
    var height =
      window.innerHeight -
      (document.getElementById("1").clientHeight +
        document.getElementById("2").clientHeight +
        document.getElementById("4").clientHeight);
    if (height < 0) {
      height = 0;
    }
    setFillerStyle({
      height: height,
    });
  }, []);

  const onNavLinkClicked = (navItem) => {
    console.log(navItem.name + ": " + navItem.url);
  };

  const renderSwitch = () => {
    var url;
    if (!window.currentURL || window.currentURL === "") {
      url = window.location.href.split(window.location.host).pop();
    } else {
      url = window.currentURL;
    }
    switch (url) {
      case "/":
        return <Home homeIntro={homeIntro} websiteIMGs={websiteIMGs} />;

      case "/projects":
        return <Projects />;
      case "/services":
        return <Services />;
      case "/certificates":
        return <Certificates />;
      case "/resume":
        return <Resume />;
      case "/contact":
        return <Contact />;
      case "/about":
        return <About />;

      default:
        break;
    }
    if (url.includes("/project?")) {
      return <Project name={url.split("name=").pop().replace(/%20/g, " ")} />;
    }
    if (url.includes("/service?")) {
      return <Service name={url.split("name=").pop().replace(/%20/g, " ")} />;
    }
    if (url.includes("/certificate?")) {
      return (
        <Certificate name={url.split("name=").pop().replace(/%20/g, " ")} />
      );
    }
  };
  return (
    <div>
      <NavBar navItems={navItems} onNavLinkClicked={onNavLinkClicked} />
      <div className="page-content" id="2">
        {renderSwitch()}
      </div>
      <div id="3" style={fillerStyle}></div>
      <Footer />
    </div>
  );
}

export default App;
