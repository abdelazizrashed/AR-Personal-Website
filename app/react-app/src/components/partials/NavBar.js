import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";

const NavBar = ({ navItems, onNavLinkClicked }) => {
  return (
    <>
      <Navbar expand="lg" className="navbar-n-footer-color" id="1">
        <Container fluid>
          <Navbar.Brand href="/">Abdelaziz Rashed</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="ms-auto">
              {navItems.map((item) => (
                <Nav.Link
                  eventKey={item.url}
                  onClick={() => {
                    onNavLinkClicked(item, item.url);
                  }}
                  href={item.url}
                  className={`${
                    item.url === window.location.pathname ? "active" : ""
                  }`}
                >
                  {item.name}
                </Nav.Link>
              ))}
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </>
  );
};

export default NavBar;
