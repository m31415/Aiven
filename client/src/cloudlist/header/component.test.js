import CloudListHeaderComponent from "./component";
import React from "react";
import { shallow } from "enzyme";

describe("CloudListHeaderComponent", () => {
  const lang = "de-DE";
  const providerFilter = "do";
  const sortDistance = true;

  let useContextSpy;
  let setProviderFilter;
  let setSortDistance;
  let tree;

  beforeEach(() => {
    setProviderFilter = jest.fn();
    setSortDistance = jest.fn();

    const testContext = {
      lang,
      providerFilter,
      setProviderFilter,
      sortDistance,
      setSortDistance
    };

    useContextSpy = jest.spyOn(React, "useContext");
    useContextSpy.mockImplementation(() => testContext);
    tree = shallow(<CloudListHeaderComponent />);
  });

  it("renders as usual", () => {
    expect(tree.debug()).toMatchSnapshot();
  });

  it("Button recieves correct variant if sortDistance", () => {
    const variant = tree.find({ name: "sortDistance" }).prop("variant");
    expect(variant).toEqual("warning");
  });

  it("Button toggles sortDistance onClick", () => {
    tree.find({ name: "sortDistance" }).simulate("click");
    expect(setSortDistance).toBeCalledWith(false);
  });

  it("Dropdown uses Provider dict to map keys to name", () => {
    const name = tree.find({ eventKey: "google" }).text();
    expect(name).toEqual("Google Cloud");
  });

  it("Dropdown Item select sets providerFilter", () => {
    tree.find("DropdownButton").simulate("select", "google");
    expect(setProviderFilter).toBeCalledWith("google");
  });
});
