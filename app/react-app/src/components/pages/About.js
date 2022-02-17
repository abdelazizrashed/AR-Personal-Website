import React from "react";

import { Row, Col, Button, Form, Image } from "react-bootstrap";
import "../../styles/About.css";
import "../../styles/Contact.css";

import "../../styles/Service.css";
import profilePic from "../../img/profile-pic.png";

const About = () => {
  return (
    <div>
      <Row>
        <Col lg={8}>
          <div className="contact-email-container" style={{ padding: "10px 60px 10px 30px" }}>
            <h1>Hello, my name is Abdelaziz Rashed</h1>
            <p style={{ fontSize: "1.5rem" }}>
              I am a software developer from Egypt. I am a senior student at the
              University of Science and Technology at Zewail City. I study
              Communication and Information Engineering. My specialization in
              college is machine intelligence and data science. <br />I am an
              enthusiastic learner. I love programming and software development.
              I have 2+ years of experience developing websites, games, and
              applications. My strongest characteristic is how fast I can learn
              and adapt. In the past 2 years, I've learned and worked with a lot
              of technologies. Today, I can take on any project no matter what
              scale it is, and I will finish in a remarkably small time.
            </p>
          </div>
        </Col>
        <Col lg={4}>
          <div
            className="contact-email-container"
            style={{ textAlign: "center" }}
          >
            <Image
              src={profilePic}
              alt="Abdelaziz Rashed profile picture"
              roundedCircle
              className="about-profile-pic"
            />
            <Button
              variant="outline-dark"
              className="project-goto-btns"
              href="/contact"
            >
              <h6>Contact me</h6>
              <i className="fas fa-chevron-right project-services-btn-icon"></i>
            </Button>
          </div>
        </Col>
      </Row>
    </div>
  );
};

export default About;
