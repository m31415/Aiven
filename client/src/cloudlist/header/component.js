import React from "react";
import DropdownButton from "react-bootstrap/DropdownButton";
import Dropdown from "react-bootstrap/Dropdown";
import Button from "react-bootstrap/Button";
import { ClientContext, cloudProviderDict } from "../../main";

const header = "Cloud Selection";

export default function CloudListHeaderComponent() {
  const {
    providerFilter,
    setProviderFilter,
    sortDistance,
    setSortDistance
  } = React.useContext(ClientContext);

  const select = selectedKey => setProviderFilter(selectedKey);
  const isFilteredByProvider = providerFilter ? "warning" : "secondary";
  const isSorted = sortDistance ? "warning" : "secondary";

  return (
    <div className="row cloudListHeader background text-center">
      <div>
        <h1 className="headerText">{header}</h1>
      </div>
      <div className="row filter">
        <p className="col">Sort by Distance</p>
        <div className="col">
          <Button
            name="sortDistance"
            variant={isSorted}
            onClick={() => setSortDistance(!sortDistance)}
          >
            <i className="fas fa-location-arrow" />
          </Button>
        </div>
      </div>
      <div className="row filter">
        <p className="col">Filter by Provider</p>
        <div className="col">
          <DropdownButton
            alignRight
            id="dropdown-menu-align-right"
            variant={isFilteredByProvider}
            onSelect={select}
            title={cloudProviderDict[providerFilter] || ""}
          >
            <Dropdown.Item key="none" eventKey={null}>
              All
            </Dropdown.Item>
            {Object.entries(cloudProviderDict).map(entry => {
              const [key, name] = entry;
              return (
                <Dropdown.Item key={key} eventKey={key}>
                  {name}
                </Dropdown.Item>
              );
            })}
          </DropdownButton>
        </div>
      </div>
    </div>
  );
}
