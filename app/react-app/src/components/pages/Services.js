import { useState } from "react";
import ServiceCard from "../components/ServiceCard";
import { Row, Col, Button } from "react-bootstrap";
import "../../styles/Services.css";

const Services = () => {
  const [noElements, setNoElements] = useState(15);
  const [startEndIndex, setStartEndIndex] = useState([0, noElements]);
  const [services, setServices] = useState([
    {
      id: "slkdjf8sduf90s8duf98sudf89sdf",
      logo: {
        src: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1280px-React-icon.svg.png",
        alt: "Image",
      },
      name: "UI design",
      description:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    },
  ]);

  const getServices = (start, end) => {
    window.scrollTo(0, 0);
  };

  const onNextPageBtnClicked = () => {
    var startI = startEndIndex[0] + noElements;
    var endI = startEndIndex[1] + noElements;
    setStartEndIndex([startI, endI]);
    getServices(startI, endI);
  };

  const onPreviousPageBtnClicked = () => {
    var startI = startEndIndex[0] - noElements;
    var endI = startEndIndex[1] - noElements;
    setStartEndIndex([startI, endI]);
    getServices(startI, endI);
  };

  getServices(startEndIndex[0], startEndIndex[1]);
  return (
    <div>
      <Row className="services-row">
        {services.slice(startEndIndex[0], startEndIndex[1]).map((service) => {
          return (
            <Col xl={4} lg={6} md={6} xs={12}>
              <ServiceCard service={service} />
            </Col>
          );
        })}
        {services.length > noElements ? (
          <div className="page-navigate-btns">
            <Button
              variant="outline-dark"
              onClick={() => onPreviousPageBtnClicked()}
              style={{ margin: "5px" }}
            >
              Previous Page
            </Button>
            <Button
              variant="outline-dark"
              onClick={() => onNextPageBtnClicked()}
              style={{ margin: "5px" }}
            >
              Next Page
            </Button>
          </div>
        ) : (
          <></>
        )}
      </Row>
      {/* <h1>Services</h1> */}
    </div>
  );
};

export default Services;
