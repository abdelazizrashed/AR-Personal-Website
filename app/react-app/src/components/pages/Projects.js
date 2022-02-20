import { useEffect, useState } from "react";
import ProjectsFilterBar from "../components/ProjectsFilterBar";
import ProjectCard from "../components/ProjectCard";
import "../../styles/Projects.css";
import { Row, Col, Button } from "react-bootstrap";
import Loading from "../components/Loading";

const Projects = () => {
  //#region Projects

  const [noElements, setNoElements] = useState(15);
  const [startEndIndex, setStartEndIndex] = useState([0, noElements]);
  const [projects, setProjects] = useState();

  useEffect(() => {
    var reqUrl =  window.apiUrl + "projects/projects?partial=true";
    var currentUrl = new URL(window.location.href);
    if(currentUrl.searchParams.get("service") != null){
      reqUrl+= "&service="+ currentUrl.searchParams.get("service");
    }
    if(currentUrl.searchParams.get("platform") != null){
      reqUrl+= "&platform="+ currentUrl.searchParams.get("platform");
    }
    if(currentUrl.searchParams.get("technology") != null){
      reqUrl+= "&technology="+ currentUrl.searchParams.get("technology");
    }
    fetch(reqUrl)
      .then((res) => res.json())
      .then((result) => {
        setIsLoading(false);
        var pjs = result.projects;
        setProjects(pjs);
      })
      .catch((error) => console.log(error));
  }, []);

  const onNextPageBtnClicked = () => {
    window.scrollTo(0, 0);
    var startI = startEndIndex[0] + noElements;
    var endI = startEndIndex[1] + noElements;
    setStartEndIndex([startI, endI]);
  };

  const onPreviousPageBtnClicked = () => {
    window.scrollTo(0, 0);
    var startI = startEndIndex[0] - noElements;
    var endI = startEndIndex[1] - noElements;
    setStartEndIndex([startI, endI]);
  };

  //#endregion
  //#region Filter bar
  //*Use state hook variables
  const [filterOptions, setFilterOptions] = useState({
    Service: {
      name: "Select Service",
      id: "0",
    },
    Platform: {
      name: "Select Platform",
      id: "0",
    },
    Technology: {
      name: "Select Technology",
      id: "0",
    },
  });

  //*Functions
  const onFilterSubmit = () => {
    const copyOfFilterOptions = { ...filterOptions };
    var url = window.apiUrl + "projects/projects?partial=true";
    var newRoute = ""
    if (copyOfFilterOptions.Service.id === "0") {
      delete copyOfFilterOptions["Service"];
    }else{
      url += "&service="+copyOfFilterOptions.Service.id;
      newRoute += "&service="+copyOfFilterOptions.Service.id;
    }
    if (copyOfFilterOptions.Platform.id === "0") {
      delete copyOfFilterOptions["Platform"];
    }else{
      url += "&platform="+copyOfFilterOptions.Platform.id;
      newRoute += "&platform="+copyOfFilterOptions.Platform.id;
    }
    if (copyOfFilterOptions.Technology.id === "0") {
      delete copyOfFilterOptions["Technology"];
    }else{
      url +="&technology="+copyOfFilterOptions.Technology.id;
      newRoute +="&technology="+copyOfFilterOptions.Technology.id;
    }
    setIsLoading(true);

    fetch(url)
      .then((res) => res.json())
      .then((result) => {
        setIsLoading(false);
        setProjects(result.projects);
        window.history.pushState("", "", newRoute);
      })
      .catch((error) => console.log(error));
  };

  //#endregion

  const [isLoading, setIsLoading] = useState(true);


  return (
    <>
      {/* <ProjectsFilterBar
        filterOptions={filterOptions}
        setFilterOptions={setFilterOptions}
        onFilterSubmit={onFilterSubmit}
      /> */}

      <Loading isLoading={isLoading} />

      {isLoading ? (
        <></>
      ) : projects == null ? (
        <></>
      ) : projects.length == 0 ? (
        <h2>No projects to display yet</h2>
      ) : (
        <Row className="projects-row">
          {projects.slice(startEndIndex[0], startEndIndex[1]).map((project) => {
            return (
              <Col xl={4} lg={6} md={6} xs={12} style={{margin:"20px auto"}}>
                <ProjectCard
                  project={project}
                  // onGoToProjectClicked={onGoToProjectClicked}
                />
              </Col>
            );
          })}
          {projects.length > noElements ? (
            <div className="page-navigate-btns">
              {startEndIndex[0] <= 0 ? (
                <></>
              ) : (
                <Button
                  variant="outline-dark"
                  onClick={() => onPreviousPageBtnClicked()}
                  style={{ margin: "100px 10px 10px" }}
                >
                  Previous Page
                </Button>
              )}
              {startEndIndex[1] >= Math.ceil(projects.length / noElements)*noElements ? (
                <></>
              ) : (
                <Button
                  variant="outline-dark"
                  onClick={() => onNextPageBtnClicked()}
                  style={{ margin: "100px 10px 10px" }}
                >
                  Next Page
                </Button>
              )}
            </div>
          ) : (
            <></>
          )}
        </Row>
      )}
    </>
  );
};

export default Projects;
