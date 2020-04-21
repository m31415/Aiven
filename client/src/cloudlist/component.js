import React from "react";
import PropTypes from "prop-types";
import CloudListHeaderComponent from "./header";
import CloudComponent from "./cloud";

export default function CloudListComponent(props) {
  const { cloudList } = props;

  return (
    <div className="container-fluid">
      <CloudListHeaderComponent />
      <div className="row justify-content-around darkBackground">
        {cloudList.map(cloudObject => {
          const { cloudName } = cloudObject;
          return <CloudComponent key={cloudName} cloudObject={cloudObject} />;
        })}
      </div>
    </div>
  );
}

CloudListComponent.propTypes = {
  cloudList: PropTypes.arrayOf(
    PropTypes.shape({
      cloudName: PropTypes.string.isRequired,
      cloudDescription: PropTypes.string.isRequired,
      geoLatitude: PropTypes.number.isRequired,
      geoLongitude: PropTypes.number.isRequired,
      geoRegion: PropTypes.string.isRequired
    })
  ).isRequired,
};
