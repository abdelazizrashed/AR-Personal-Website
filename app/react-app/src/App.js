import "./styles/App.css";
import NavBar from "./components/partials/NavBar";
import Footer from "./components/partials/Footer";
import Home from "./components/pages/Home";
import About from "./components/pages/About";
import Projects from "./components/pages/Projects";
import Services from "./components/pages/Services";
import Certificates from "./components/pages/Certificates";
import Contact from "./components/pages/Contact";
import Resume from "./components/pages/Resume";

function App() {
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
        return <Home />;

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
