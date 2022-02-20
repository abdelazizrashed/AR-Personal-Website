import { Row, Col, Carousel, Button, Image } from "react-bootstrap";
import { useState, useEffect } from "react";
import Loading from "../components/Loading";
import "../../styles/Project.css";

const Project = ({ name }) => {
  const [isLoading, setIsLoading] = useState(true);
  const [project, setProject] = useState();

  useEffect(() => {
    var reqUrl = window.apiUrl + "projects/project?partial=false";
    var currentUrl = new URL(window.location.href);
    if (currentUrl.searchParams.get("id") != null) {
      reqUrl += "&id=" + currentUrl.searchParams.get("id");
    }
    fetch(reqUrl)
      .then((res) => res.json())
      .then((result) => {
        setIsLoading(false);
        console.log(result);
        setProject(result);
      })
      .catch((error) => console.log(error));
  }, []);

  return (
    <div>
      <Loading isLoading={isLoading} />
      {isLoading ? (
        <></>
      ) : project == null ? (
        <></>
      ) : (
        <>
          <Row>
            <Col lg={8}>
              <Carousel className="project-carousel">
                {project.imgs == null ? (
                  <></>
                ) : (
                  project.imgs.map((img) => {
                    return (
                      <Carousel.Item interval={1000}>
                        <img
                          className="d-block w-100"
                          src={img.src}
                          alt={img.alt}
                          style={{
                            height: "500px",
                            objectFit: "contain"
                          }}
                        />
                        <Carousel.Caption>
                          <h3>{img.caption}</h3>
                        </Carousel.Caption>
                      </Carousel.Item>
                    );
                  })
                )}
              </Carousel>
              <iframe
                width="853"
                height="480"
                src={project.youtubeVid.src}
                title={project.youtubeVid.title}
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
                className="project-vid"
              ></iframe>
            </Col>
            <Col lg={4}>
              <div className="project-info">
                <h1>{project.name}</h1>
                <p>{project.description}</p>
                {project.appStoreUrl && project.appStoreUrl !== "" ? (
                  <Button
                    variant="outline-dark"
                    className="project-goto-btns"
                    href={project.appStoreUrl}
                  >
                    Download <i class="fab fa-apple project-goto-btns-icon"></i>
                  </Button>
                ) : (
                  <></>
                )}
                {project.googlePlayStoreUrl &&
                project.googlePlayStoreUrl !== "" ? (
                  <Button
                    variant="outline-dark"
                    className="project-goto-btns"
                    href={project.googlePlayStoreUrl}
                  >
                    Download{" "}
                    <i class="fab fa-google-play project-goto-btns-icon"></i>
                  </Button>
                ) : (
                  <></>
                )}
                {project.githubUrl && project.githubUrl !== "" ? (
                  <Button
                    variant="outline-dark"
                    className="project-goto-btns"
                    href={project.githubUrl}
                  >
                    Get Code{" "}
                    <i class="fab fa-github project-goto-btns-icon"></i>
                  </Button>
                ) : (
                  <></>
                )}
                {project.websiteUrl && project.websiteUrl !== "" ? (
                  <Button
                    variant="outline-dark"
                    className="project-goto-btns"
                    href={project.websiteUrl}
                  >
                    Visit Website{" "}
                    <i class="fas fa-browser project-goto-btns-icon"></i>
                  </Button>
                ) : (
                  <></>
                )}
              </div>
              {project.services == null ? (
                <></>
              ) : (
                <div className="project-services">
                  <h1>Services Provided</h1>
                  {project.services.map((service) => {
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
                          caption={service.logo.caption}
                          roundedCircle
                          className="project-services-btn-logo"
                        />
                        <h6>{service.name}</h6>
                        <i className="fas fa-chevron-right project-services-btn-icon"></i>
                      </Button>
                    );
                  })}
                </div>
              )}
            </Col>
          </Row>
          <Row>
            <Col lg={8}>
              <div className="project-services">
                <h1>Details</h1>
                <div className="project-details-div">
                  {project.detailedServices.details == null ? (
                    <></>
                  ) : project.detailedServices.details.length <= 0 ? (
                    <></>
                  ) : (
                    <>
                      <h2>Services</h2>
                      <ul className="project-details-ul">
                        {project.detailedServices.details.map((service) => {
                          return (
                            <li>
                              <h4>{service.name}</h4>
                              <p>{service.description}</p>
                            </li>
                          );
                        })}
                      </ul>
                    </>
                  )}
                  {project.detailedTechnologies.details == null ? (
                    <></>
                  ) : project.detailedTechnologies.details.length <= 0 ? (
                    <></>
                  ) : (
                    <>
                      <h2>Technologies</h2>
                      <ul className="project-details-ul">
                        {project.detailedTechnologies.details.map(
                          (technology) => {
                            return (
                              <li>
                                <h4>{technology.name}</h4>
                                <p>{technology.description}</p>
                              </li>
                            );
                          }
                        )}
                      </ul>
                    </>
                  )}

                  {project.detailedPlatforms.details == null ? (
                    <></>
                  ) : project.detailedPlatforms.details.length > 0 ? (
                    <>
                      <h2>Platforms</h2>
                      <ul className="project-details-ul">
                        {project.detailedPlatforms.details.map((platform) => {
                          return (
                            <li>
                              <h4>{platform.name}</h4>
                              <p>{platform.description}</p>
                            </li>
                          );
                        })}
                      </ul>
                    </>
                  ) : (
                    <></>
                  )}
                </div>
              </div>
            </Col>
            <Col lg={4}>
              {project.relatedProjects == null ? (
                <></>
              ) : project.relatedProjects.length > 0 ? (
                <div className="project-services">
                  <h1>Other Related Projects</h1>
                  {project.relatedProjects.map((project) => {
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
            </Col>
          </Row>
        </>
      )}
    </div>
  );
};

export default Project;
