import { Card, Button } from "react-bootstrap";

const ProjectCard = ({ project, onGoToProjectClicked }) => {
  return (
    <Card className="project-card">
      <div className="project-img">
        <Card.Img variant="top" src={project.imgURL} />
      </div>
      <Card.Body>
        <Card.Title className="project-title">{project.name}</Card.Title>
        <h6>Platforms:</h6>
        <ul className="project-ul">
          {project.platforms.slice(0, 3).map((platform) => {
            return <li>{platform}</li>;
          })}
          {project.platforms.length > 3 ? <h6>...</h6> : <></>}
        </ul>
        <h6>Technologies:</h6>
        <ul className="project-ul">
          {project.technologies.slice(0, 3).map((technology) => {
            return <li>{technology}</li>;
          })}
          {project.technologies.length > 3 ? <h6>...</h6> : <></>}
        </ul>
        <Button
          variant="outline-dark"
          className="go-to-project-btn"
          onClick={() => onGoToProjectClicked(project)}
          //   /project?id=1&name=new-project
          href={"/project?id=" + project.id + "&name=" + project.name}
        >
          Go To Project <i class="fas fa-chevron-right"></i>
        </Button>
      </Card.Body>
    </Card>
  );
};

export default ProjectCard;
