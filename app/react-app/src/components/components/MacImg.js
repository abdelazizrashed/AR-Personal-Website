import React from "react";
import macbook from "../../img/macbook.png";
import "../../styles/HomeImgs.css";

const MacImg = ({ websiteIMG }) => {
  return (
    <div>
      <div>
        <img
          src={websiteIMG.url}
          alt={websiteIMG.alt}
          className="website-inside-mac"
        />
      </div>
      <img src={macbook} className="macbook-img" alt="Macbook png" />
    </div>
  );
};

export default MacImg;
