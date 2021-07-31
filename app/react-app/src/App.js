import "./styles/App.css";
import { useState } from "react";
import NavBar from "./components/partials/NavBar";
import Footer from "./components/partials/Footer";
import Home from "./components/pages/Home";
import About from "./components/pages/About";
import Projects from "./components/pages/Projects";
import Services from "./components/pages/Services";
import Certificates from "./components/pages/Certificates";
import Contact from "./components/pages/Contact";
import Resume from "./components/pages/Resume";
import psPC from "./img/ps-pc.png";
import psIpad from "./img/ps-phone.png";

function App() {
  // UseState hook variables
  const [websiteIMGs, setWebsiteIMGs] = useState({
    mac: window.info.homeLaptopImgInfo,
    ipad: window.info.homeTabletImgInfo,
    phone: window.info.homePhoneImgInfo,
  });
  var isFalse = false === true;
  const [navItems, setNavItems] = useState(window.navItems);

  const [homeIntro, setHomeIntro] = useState(
    "Freelance Software Developer from Egypt. \nHighly experienced in Full-Stack Web Development, Game Development, and Cross-Platform App Development."
  );

  //Function variables
  const onNavLinkClicked = (navItem) => {
    console.log(navItem.name + ": " + navItem.url);
  };

  const renderSwitch = () => {
    var url;
    if (!window.currentURL || window.currentURL === "") {
      url = window.location.pathname;
    } else {
      url = window.currentURL;
    }
    console.log(url);
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
  };
  return (
    <div>
      <NavBar navItems={navItems} onNavLinkClicked={onNavLinkClicked} />
      {renderSwitch()}
      <Footer />
    </div>
  );
}

export default App;
