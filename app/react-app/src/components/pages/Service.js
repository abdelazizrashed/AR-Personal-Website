import { Row, Col, Button, Image } from "react-bootstrap";
import "../../styles/Service.css";

const Service = ({ name }) => {
  const service = {
    name: "UI design",
    logo: {
      src: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1280px-React-icon.svg.png",
      alt: "Image",
    },
    description:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    projects: [
      {
        name: "Slkdf jsldkf",
        id: "8d98fsd98fsfd",
      },
      {
        name: "Slkdf jsldkf",
        id: "8d98fsd98fsfd",
      },
      {
        name: "Slkdf jsldkf",
        id: "8d98fsd98fsfd",
      },
      {
        name: "Slkdf jsldkf",
        id: "8d98fsd98fsfd",
      },
    ],
    otherServices: [
      {
        name: "UI design",
        logoURL:
          "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1280px-React-icon.svg.png",
        href: "/service?id=lkjsdlksdjslkdjlsk&name=UI%20design",
      },
      {
        name: "Front-end development",
        logoURL:
          "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/5YhXXuS0hIw6JV3nJr3GgP/682bf2a70a98c3e466f26c2c2a812d65/front-end-web-developer-nanodegree--nd001.jpg",
        href: "/service?id=lkjsdlksdjslkdjlsk&name=Front-end%20development",
      },
      {
        name: "Back-end development",
        logoURL:
          "data:image/jpeg;base64,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",
        href: "/service?id=lkjsdlksdjslkdjlsk&name=Back-end development",
      },
    ],
    content: [
      {
        title: "Velit ut tortor pretium",
        paragraph:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Elit scelerisque mauris pellentesque pulvinar pellentesque. Adipiscing tristique risus nec feugiat in fermentum posuere urna.",
      },
      {
        title: "Velit ut tortor pretium",
        paragraph:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Elit scelerisque mauris pellentesque pulvinar pellentesque. Adipiscing tristique risus nec feugiat in fermentum posuere urna.",
      },
      {
        title: "Velit ut tortor pretium",
        paragraph:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Elit scelerisque mauris pellentesque pulvinar pellentesque. Adipiscing tristique risus nec feugiat in fermentum posuere urna.",
      },
    ],
    technologies: [
      {
        name: "ReactJS",
        description:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Viverra mauris in aliquam sem fringilla ut morbi tincidunt.",
      },
      {
        name: "Flask",
        description:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Viverra mauris in aliquam sem fringilla ut morbi tincidunt.",
      },
    ],
  };

  return (
    <div>
      <Row>
        <Col lg={8}>
          <div className="service-content">
            {service.content.length > 0 ? (
              service.content.map((element) => {
                return (
                  <>
                    <h2>{element.title}</h2>
                    <p>{element.paragraph}</p>
                  </>
                );
              })
            ) : (
              <></>
            )}

            <h2>Technologies</h2>
            <ul className="project-details-ul">
              {service.technologies.map((technology) => {
                return (
                  <li>
                    <h4>{technology.name}</h4>
                    <p>{technology.description}</p>
                  </li>
                );
              })}
            </ul>
          </div>
        </Col>
        <Col lg={4}>
          <div className="project-info">
            <Image
              src={service.logo.src}
              alt={service.logo.alt}
              roundedCircle
              className="service-card-logo"
            />
            <h1>{service.name}</h1>
            <p>{service.description}</p>
            <Button
              variant="outline-dark"
              className="project-goto-btns"
              href="/contact"
            >
              <h6>Contact me</h6>
              <i className="fas fa-chevron-right project-services-btn-icon"></i>
            </Button>
          </div>

          {service.projects.length > 0 ? (
            <div className="project-services">
              <h1>Projects</h1>
              {service.projects.map((project) => {
                return (
                  <Button
                    variant="outline-dark"
                    className="project-goto-btns"
                    href={"/project?id=" + project.id + "&name=" + project.name}
                  >
                    <h6>{project.name}</h6>
                    <i className="fas fa-chevron-right project-services-btn-icon"></i>
                  </Button>
                );
              })}
            </div>
          ) : (
            <></>
          )}
          {service.otherServices.length > 0 ? (
            <div className="project-services">
              <h1>Other Services</h1>
              {service.otherServices.map((service) => {
                return (
                  <Button
                    variant="outline-dark"
                    className="project-goto-btns"
                    href={service.href}
                  >
                    <Image
                      src={service.logoURL}
                      roundedCircle
                      className="project-services-btn-logo"
                    />
                    <h6>{service.name}</h6>
                    <i className="fas fa-chevron-right project-services-btn-icon"></i>
                  </Button>
                );
              })}
            </div>
          ) : (
            <></>
          )}
        </Col>
      </Row>
    </div>
  );
};

export default Service;
