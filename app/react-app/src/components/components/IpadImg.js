import React from "react";
import ipad from "../../img/Ipad.png";
import psPhone from "../../img/ps-phone.png";
import "../../styles/HomeImgs.css";

const IpadImg = () => {
  return (
    <div>
      <div>
        <img
          src={psPhone}
          alt="Website on tablet"
          className="website-inside-ipad"
        />
        {/* <img
          src={psPhone}
          alt="Website on a phone"
          className="website-inside-phone"
        /> */}
      </div>
      <img src={ipad} alt="Ipad png " className="ipad-img" />;
    </div>
  );
};

export default IpadImg;
