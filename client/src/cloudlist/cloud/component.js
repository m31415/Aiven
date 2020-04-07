import React from "react";
import PropTypes from "prop-types";
import { ClientContext } from "../../main";

export default function CloudComponent(props) {
  const {
    cloudObject: { cloudName, cloudDescription, distance }
  } = props;
  const { lang } = React.useContext(ClientContext);

  const distanceFormatted = distance
    ? `Distance: ${distance.toLocaleString(lang, {
        maximumFractionDigits: 2
      })} Km`
    : null;

  return (
    <div
      id="cloudContainer"
      className={`
      col-10 mb-4 mt-4
      col-sm-5 m-sm-4
      col-lg-3 m-lg-1 mt-lg-4 mb-lg-4
      p-3
      card background`}
    >
      <div id="cloudBody" className="card-body">
        <h5 className="card-title">{cloudName}</h5>
        <span className="row">
          <p className="col">{cloudDescription}</p>
        </span>
        <span className="row cloudDistance">
          <p className="col text-center">{distanceFormatted}</p>
        </span>
      </div>
    </div>
  );
}

CloudComponent.propTypes = {
  cloudObject: PropTypes.shape({
    cloudName: PropTypes.string.isRequired,
    cloudDescription: PropTypes.string.isRequired,
    geoRegion: PropTypes.string.isRequired,
    distance: PropTypes.number
  }).isRequired
};
