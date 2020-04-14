import React from "react";
import CloudListComponent from "./cloudlist";
import camelcaseKeysDeep from "camelcase-keys-deep";

export const cloudProviderDict = {
  aws: "Amazon Web Services",
  do: "Digital Ocean",
  google: "Google Cloud",
  azure: "Azure",
  upcloud: "UpCloud"
};

// geolocation.getCurrentPosition seems to be pretty flimsy
// and is not supported without https (relevant for deployment)
// A better fallback solution could be implementing 3rd party service like
// https://ipinfo.io/ but this would be out of scope I guess
const fallBackGeoLocation = {
  lat: 52.520008,
  lng: 13.404954
};

export const ClientContext = React.createContext();

export default function MainComponent(props) {
  const lang = navigator.lang;
  const [currentPosition, setCurrentPosition] = React.useState(null);
  const [sortDistance, setSortDistance] = React.useState(false);
  const [cloudList, setCloudList] = React.useState([]);
  const [providerFilter, setProviderFilter] = React.useState(null);

  navigator.geolocation.getCurrentPosition(
    position => {
      setCurrentPosition([position.coords.latitude, position.coords.longitude]);
    },
    () => {
      setCurrentPosition([fallBackGeoLocation.lat, fallBackGeoLocation.lng]);
    },
    { maximumAge: 2000, timeout: 5000 }
  );

  React.useEffect(() => {
    const params = {};
    if (providerFilter) {
      params.provider = providerFilter;
    }
    if (sortDistance && currentPosition) {
      params.lat = currentPosition[0];
      params.lng = currentPosition[1];
    }
    fetch("/api/clouds?" + new URLSearchParams(params))
      .then(response => {
        return response.json();
      })
      .then(result => {
        setCloudList(camelcaseKeysDeep(result));
      });
  }, [providerFilter, sortDistance, currentPosition]);

  return (
    <ClientContext.Provider
      value={{
        lang,
        providerFilter,
        setProviderFilter,
        sortDistance,
        setSortDistance
      }}
    >
      <CloudListComponent lang={lang} cloudList={cloudList} />
    </ClientContext.Provider>
  );
}
