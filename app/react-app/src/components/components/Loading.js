
import "../../styles/Loading.css"
import ClipLoader from "react-spinners/ClipLoader";
// import { css } from "@emotion/react";

function Loading({isLoading}) {

    return ( 
        <div className="loading-bars">
            <ClipLoader color="#b5eaea" loading={isLoading} size={50} />
        </div>
     );
}

export default Loading;