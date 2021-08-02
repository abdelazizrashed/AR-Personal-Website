import { useState } from "react";
import ProjectsFilterBar from "../components/ProjectsFilterBar";
import ProjectCard from "../components/ProjectCard";
import "../../styles/Projects.css";
import psPC from "../../img/ps-pc.png";
import { Row, Col } from "react-bootstrap";

const Projects = () => {
  //Todo: make a request to the backend api to get the projects

  //#region Projects

  const projects = [
    {
      name: "Abdelaziz Rashed Personal Website",
      platforms: [
        "iOS",
        "Android",
        "Android",
        "Android",
        "Android",
        "Android",
        "Android",
        "Android",
        "Android",
      ],
      technologies: ["ReactJS", "Flask", "HTML", "CSS", "Bootstrap"],
      imgURL: psPC,
      id: "920348jdoisdfw9e8fsdiof",
    },
  ];

  const onGoToProjectClicked = (project) => {
    console.log(project);
  };

  //#endregion
  //#region Filter bar
  //*Use state hook variables
  const [filterOptions, setFilterOptions] = useState({
    Service: {
      name: "Select Service",
      key: "0",
    },
    Platform: {
      name: "Select Platform",
      key: "0",
    },
    Technology: {
      name: "Select Technology",
      key: "0",
    },
  });

  const [searchInputValue, setSearchInputValue] = useState();

  //*Functions
  const onFilterSubmit = () => {
    const copyOfFilterOptions = { ...filterOptions };
    if (copyOfFilterOptions.Service.key === "0") {
      delete copyOfFilterOptions["Service"];
    }
    if (copyOfFilterOptions.Platform.key === "0") {
      delete copyOfFilterOptions["Platform"];
    }
    if (copyOfFilterOptions.Technology.key === "0") {
      delete copyOfFilterOptions["Technology"];
    }
    console.log(copyOfFilterOptions);
    //Todo: send request to api to fetch data with this filter
    // setValidated(true);
  };

  //#endregion

  const onSearchBtnClicked = () => {
    console.log(searchInputValue);
  };
  return (
    <div>
      <ProjectsFilterBar
        filterOptions={filterOptions}
        setFilterOptions={setFilterOptions}
        onFilterSubmit={onFilterSubmit}
        setSearchInputValue={setSearchInputValue}
        onSearchBtnClicked={onSearchBtnClicked}
      />
      <Row className="projects-row">
        {projects.map((project) => {
          return (
            <Col xl={4} lg={6} sm={12}>
              <ProjectCard
                project={project}
                onGoToProjectClicked={onGoToProjectClicked}
              />
            </Col>
          );
        })}
      </Row>
    </div>
  );
};

export default Projects;
