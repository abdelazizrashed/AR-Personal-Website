import { useState, useEffect } from "react";
import { Row, Col, Button, Image } from "react-bootstrap";
import "../../styles/Service.css";
import Loading from "../components/Loading";

const Service = () => {
  const [service, setService] = useState();
  const [isLoading, setIsLoading] = useState();

  useEffect(() => {
    var reqUrl = window.apiUrl + "services/service?partial=false";
    var currentUrl = new URL(window.location.href);
    if (currentUrl.searchParams.get("id") != null) {
      reqUrl += "&id=" + currentUrl.searchParams.get("id");
    }
    fetch(reqUrl)
      .then((res) => res.json())
      .then((result) => {
        console.log(result);
        // var  copy
        if (result.projectsIds) {
          result.projects = [];
          result.projectsIds.forEach((id_) => {
            fetch(window.apiUrl + "projects/project?partial=true&id=" + id_)
              .then((res) => res.json())
              .then((data) => {
                result.projects.push(data);
              })
              .catch((error) => console.log(error));
          });
        }
        if (result.otherServicesIds) {
          result.otherServices = [];
          result.otherServicesIds.forEach((id_) => {
            fetch(window.apiUrl + "services/service?partial=true&id=" + id_)
              .then((res) => res.json())
              .then((data) => {
                result.otherServices.push(data);
              })
              .catch((error) => console.log(error));
          });
        }
        setIsLoading(false);
        setService(result);
      })
      .catch((error) => console.log(error));
  }, []);

  return (
    <div>
      <Loading isLoading={isLoading} />
      {isLoading ? (
        <></>
      ) : service == null ? (
        <></>
      ) : (
        <>
          <Row>
            <Col lg={8}>
              <div className="service-content">
                {service.content == null ? (
                  <></>
                ) : service.content.length > 0 ? (
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
                {service.technologies == null ? (
                  <></>
                ) : service.technologies.length == 0 ? (
                  <></>
                ) : (
                  <>
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
                  </>
                )}
              </div>
            </Col>
            <Col lg={4}>
              <div className="project-info">
                <Image
                  src={service.logo.src}
                  alt={service.logo.alt}
                  caption={service.logo.caption}
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

              {service.projects == null ? (
                <></>
              ) : service.projects.length > 0 ? (
                <div className="project-services">
                  <h1>Projects</h1>
                  {service.projects.map((project) => {
                    return (
                      <Button
                        variant="outline-dark"
                        className="project-goto-btns"
                        href={
                          "/project?id=" + project.id + "&name=" + project.name
                        }
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
              {service.otherServices == null ? (
                <></>
              ) : service.otherServices.length > 0 ? (
                <div className="project-services">
                  <h1>Other Services</h1>
                  {service.otherServices.map((service) => {
                    return (
                      <Button
                        variant="outline-dark"
                        className="project-goto-btns"
                        href={
                          "/service?id=" + service.id + "&name=" + service.name
                        }
                      >
                        <Image
                          src={service.logo.src}
                          alt={service.logo.alt}
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
        </>
      )}
    </div>
  );
};

export default Service;
