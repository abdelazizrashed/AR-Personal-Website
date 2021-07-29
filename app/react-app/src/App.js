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
  const [websiteIMGs, setWebsiteIMGs] = useState({
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
  });
  const [homeIntro, setHomeIntro] = useState(
    "Freelance Software Developer from Egypt. \nHighly experienced in Full-Stack Web Development, Game Development, and Cross-Platform App Development."
  );

  const onNavLinkClicked = (navItem) => {
    console.log(navItem.name + ": " + navItem.url);
  };
  const navItems = [
    { name: "Home", url: "/" },
    {
      name: "Projects",
      url: "/projects",
    },
    {
      name: "Services",
      url: "/services",
    },
    {
      name: "Certificates",
      url: "/certificates",
    },
    {
      name: "Resume",
      url: "/resume",
    },
    {
      name: "Contact",
      url: "/contact",
    },
    {
      name: "About",
      url: "/about",
    },
  ];

  const renderSwitch = () => {
    switch (window.location.pathname) {
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
      case "/conact":
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
