/* eslint-disable no-unused-vars */
import "./styles/App.css";
import { useState, useEffect, useLayoutEffect } from "react";
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

function App() {

  var domainName =  window.location.href
  // window.apiUrl = "http://127.0.0.1:5000/api/";
  window.apiUrl = "api/";


  var nav = [
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
      name: "About",
      url: "/about",
    }
  ];
  // if (!window.navItems || window.navItems === "") {
  //   nav = 
  // } else {
  //   nav = window.navItems;
  // }
  const [navItems, setNavItems] = useState(nav);

  const [homeIntro, setHomeIntro] = useState(
    "Freelance Software Developer from Egypt. \nHighly experienced in Full-Stack Web Development, Game Development, and Cross-Platform App Development."
  );

  const [fillerStyle, setFillerStyle] = useState({});

  //Function variables
  useEffect(() => {
    function handleResize(){
      var height =
        window.innerHeight -
        (document.getElementById("1").clientHeight +
          document.getElementById("4").clientHeight);
      if (height < 0) {
        height = 0;
      }
      setFillerStyle({
        minHeight: height,
      });
    }
    window.addEventListener("resize", handleResize);
    handleResize();
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
        return <Home homeIntro={homeIntro} /*websiteIMGs={websiteIMGs} */domainName={domainName}/>;

      case "/projects":
        return <Projects domainName={domainName}/>;
      case "/services":
        return <Services domainName={domainName}/>;
      case "/certificates":
        return <Certificates domainName={domainName}/>;
      case "/resume":
        return <Resume domainName={domainName}/>;
      case "/contact":
        return <Contact domainName={domainName}/>;
      case "/about":
        return <About domainName={domainName}/>;

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
  // console.log(window.location.href)
  return (
    <div>
      <NavBar navItems={navItems} onNavLinkClicked={onNavLinkClicked} />
      <div className="page-content" id="2" style={fillerStyle}>
        {renderSwitch()}
      </div>
      <Footer />
      {/* <div className="footer-container">
      </div> */}
    </div>
  );
}

export default App;
