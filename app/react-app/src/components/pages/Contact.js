/* eslint-env browser */
import React from "react";
import { init, send } from "@emailjs/browser";
import { Row, Col, Button, Form } from "react-bootstrap";
import "../../styles/Contact.css";
import "../../styles/Home.css";

const Contact = () => {
  init("user_kZ7YqwByGmztJh8eUd1tb");
  const onContactFormSubmit = (e) => {
    e.preventDefault();
    // getElementById('main').getElementsByClassName('test')
    // .getElementById('contactFormName').getElementsByClassName('form-control').value
    // console.log(e.target[0].value)
    const name = e.target[0].value;
    const email = e.target[1].value;
    const purpose = e.target[2].value;
    const message = e.target[3].value;
    const variables = {
      from_name: name,
      from_email: email,
      purpose: purpose,
      message: message,
    };
    // window.emailjs
    send("service_71lybhd", "template_13kdewe", variables)
      .then((res) => {
        console.log("Email successfully sent!");
      })
      // Handle errors here however you like, or use a React error boundary
      .catch((err) =>
        console.error(
          "Oh well, you failed. Here some thoughts on the error that occured:",
          err
        )
      );
  };

  return (
    <div>
      <p class="home-intro">
        If you want to get in touch, talk to me about a project collaboration or
        just to say hi, fill-up the form below.
      </p>
      <Row>
        <Col lg={8}>
          <div className="contact-email-container">
            <Form onSubmit={onContactFormSubmit}>
              <Row>
                <Col>
                  <Form.Group className="mb-3" controlId="contactFormName">
                    <Form.Label style={{ display: "block" }}>Name</Form.Label>
                    <Form.Control
                      type="text"
                      style={{ display: "block", width: "100%" }}
                    />
                  </Form.Group>
                </Col>
                <Col>
                  <Form.Group className="mb-3" controlId="contactFormEmail">
                    <Form.Label style={{ display: "block" }}>
                      Email address
                    </Form.Label>
                    <Form.Control
                      type="email"
                      style={{ display: "block", width: "100%" }}
                    />
                  </Form.Group>
                </Col>
              </Row>
              <Row>
                <Form.Group className="mb-3" controlId="contactFormPurpose">
                  <Form.Label style={{ display: "block" }}>Purpose</Form.Label>
                  <Form.Control
                    type="text"
                    style={{ display: "block", width: "100%" }}
                  />
                </Form.Group>
              </Row>
              <Row>
                <Form.Group className="mb-3" controlId="contactFromMessage">
                  <Form.Label style={{ display: "block" }}>Message</Form.Label>
                  <Form.Control
                    as="textarea"
                    rows={5}
                    style={{ display: "block", width: "100%" }}
                  />
                </Form.Group>
              </Row>

              <Button
                variant="outline-primary"
                type="submit"
                style={{ display: "block", margin: "auto", width: "30%" }}
              >
                Submit
              </Button>
            </Form>
          </div>
        </Col>
        <Col lg={4}>
          <div className="contact-socail-container">
            <h3>Let's get social</h3>
            <a href="https://wa.me/message/JQC5TF6DHOB6B1">
              <i class="fab fa-whatsapp social-icons"></i>
            </a>
            <a href="https://www.linkedin.com/in/abdelaziz-y-rashed/">
              <i class="fab fa-linkedin social-icons"></i>
            </a>
            <a href="https://www.facebook.com/abde1aziz/">
              <i class="fab fa-facebook social-icons"></i>
            </a>
            <a href="https://m.me/abde1aziz">
              <i class="fab fa-facebook-messenger social-icons"></i>
            </a>
            <a href="https://github.com/abdelazizrashed">
              <i class="fab fa-github social-icons"></i>
            </a>
          </div>
        </Col>
      </Row>
    </div>
  );
};

export default Contact;
