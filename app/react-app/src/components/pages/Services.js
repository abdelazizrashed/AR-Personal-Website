// import { useState } from "react";
import ServiceCard from "../components/ServiceCard";
import { Row, Col } from "react-bootstrap";
import "../../styles/Services.css";

const Services = () => {
  const services = [
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
  ];
  return (
    <div>
      <Row className="services-row">
        {services.map((service) => {
          return (
            <Col xl={4} lg={6} md={6} xs={12}>
              <ServiceCard service={service} />
            </Col>
          );
        })}
      </Row>
      {/* <h1>Services</h1> */}
    </div>
  );
};

export default Services;
