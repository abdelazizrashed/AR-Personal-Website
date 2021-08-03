import { Card, Button, Image } from "react-bootstrap";

const ServiceCard = ({ service, onGoToServiceClicked }) => {
  return (
    <Card className="service-card">
      <Image
        src={service.logoURL}
        roundedCircle
        className="service-card-logo"
      />
      <Card.Body>
        <Card.Title className="project-title">{service.name}</Card.Title>
        <Card.Text className="service-description">{service.description}</Card.Text>
        <Button
          variant="outline-dark"
          className="go-to-service-btn"
          onClick={() => onGoToServiceClicked(service)}
          href={"/service?id=" + service.id + "&name=" + service.name}
        >
          Go To Service <i class="fas fa-chevron-right"></i>
        </Button>
      </Card.Body>
    </Card>
  );
};

export default ServiceCard;
