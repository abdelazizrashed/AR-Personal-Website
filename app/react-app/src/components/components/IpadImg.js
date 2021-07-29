import React from "react";
import ipad from "../../img/Ipad.png";
import "../../styles/HomeImgs.css";

const IpadImg = ({ websiteIMG }) => {
  return (
    <div>
      <div>
        <img
          src={websiteIMG.url}
          alt={websiteIMG.alt}
          className="website-inside-ipad"
        />
      </div>
      <img src={ipad} alt="Ipad png " className="ipad-img" />;
    </div>
  );
};

export default IpadImg;
