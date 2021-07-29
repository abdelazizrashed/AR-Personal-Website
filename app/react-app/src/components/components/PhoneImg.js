import React from "react";
import phone from "../../img/phone.png";
import "../../styles/HomeImgs.css";

const PhoneImg = ({ websiteIMG }) => {
  return (
    <div>
      <div>
        <img
          src={websiteIMG.url}
          alt={websiteIMG.alt}
          className="website-inside-phone"
        />
      </div>
      <img src={phone} alt="Phone png" className="phone-img" />
    </div>
  );
};

export default PhoneImg;
