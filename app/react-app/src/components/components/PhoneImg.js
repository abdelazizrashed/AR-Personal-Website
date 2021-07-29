import React from "react";
import phone from "../../img/phone.png";
import psPhone from "../../img/ps-phone.png";
import "../../styles/HomeImgs.css";

const PhoneImg = () => {
  return (
    <div>
      <div>
        {/* <img
          src={psPhone}
          alt="Website on a phone"
          className="website-inside-phone"
        /> */}
      </div>
      <img src={phone} alt="Phone png" className="phone-img" />
    </div>
  );
};

export default PhoneImg;
