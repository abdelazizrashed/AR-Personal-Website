import { useEffect, useState } from "react";
import {
  Form,
  Button,
  Dropdown,
  DropdownButton,
  ButtonGroup,
} from "react-bootstrap";

const ProjectsFilterBar = ({
  filterOptions,
  setFilterOptions,
  onFilterSubmit
}) => {
  //Todo: send request to the back end api to fetch all data
  
  const [serviceOptions, setServiceOptions] = useState();
  const [platformOptions, setPlatformOptions] = useState();
  const [technologyOptions, setTechnologyOptions] =  useState();

  useEffect(() => {
    fetch(window.apiUrl + "services/services?partial=true")
      .then((res) => res.json())
      .then((result) => {
        setServiceOptions(result.services);
      })
      .catch((error) => console.log(error));
    fetch(window.apiUrl + "shared/technologies?partial=true")
      .then((res) => res.json())
      .then((result) => {
        setTechnologyOptions(result.technologies)
      })
      .catch((error) => console.log(error));
    fetch(window.apiUrl + "shared/platforms?partial=true")
      .then((res) => res.json())
      .then((result) => {
        setPlatformOptions(result.platforms)
      })
      .catch((error) => console.log(error));
  }, []);

  return (
    <div className="filter-bar">
      <Form>
        <DropdownButton
          as={ButtonGroup}
          key="Service"
          id="dropdown-variants-Service"
          variant="outline-dark"
          // style={{ maxHeight: "28px" }}
          title={<p>{filterOptions.Service.name}</p>}
          onSelect={(value) => {
            const copyOfFilterOptions = { ...filterOptions };
            delete copyOfFilterOptions["Service"];
            setFilterOptions({
              ...copyOfFilterOptions,
              Service: {
                name:
                  value === "0"
                    ? "Select Service"
                    : serviceOptions.filter((option) => {
                        return option.id === value ? option.name : null;
                      })[0].name,
                id: value,
              },
            });
          }}
        >
          <Dropdown.Item
            eventKey="0"
            active={filterOptions.Service.id === "0"}
          >
            Select Service
          </Dropdown.Item>
          {serviceOptions  == null? null: serviceOptions.map((option) => {
            return (
              <Dropdown.Item
                eventKey={option.id}
                active={filterOptions.Service.id === option.id}
              >
                {option.name}
              </Dropdown.Item>
            );
          })}
        </DropdownButton>
        <DropdownButton
          as={ButtonGroup}
          key="Platform"
          id="dropdown-variants-Platform"
          variant="outline-dark"
          title={<p>{filterOptions.Platform.name}</p>}
          onSelect={(value) => {
            const copyOfFilterOptions = { ...filterOptions };
            delete copyOfFilterOptions["Platform"];
            setFilterOptions({
              ...copyOfFilterOptions,
              Platform: {
                name:
                  value === "0"
                    ? "Select Platform"
                    : platformOptions.filter((option) => {
                      console.log(value);
                        return option.id === value ? option.name : null;
                      })[0].name,
                id: value,
              },
            });
          }}
        >
          <Dropdown.Item
            eventKey="0"
            active={filterOptions.Platform.id === "0" }
          >
            Select Platform
          </Dropdown.Item>
          {platformOptions == null? null: platformOptions.map((option) => {
            return (
              <Dropdown.Item
                eventKey={option.id}
                active={
                  filterOptions.Platform.id === option.id 
                }
              >
                {option.name}
              </Dropdown.Item>
            );
          })}
        </DropdownButton>
        <DropdownButton
          as={ButtonGroup}
          key="Technology"
          id="dropdown-variants-Technology"
          variant="outline-dark"
          size="10"
          title={<p>{filterOptions.Technology.name}</p>}
          onSelect={(value) => {
            const copyOfFilterOptions = { ...filterOptions };
            delete copyOfFilterOptions["Technology"];
            setFilterOptions({
              ...copyOfFilterOptions,
              Technology: {
                name:
                  value === "0"
                    ? "Select Technology"
                    : technologyOptions.filter((option) => {
                        return option.id === value ? option.name : null;
                      })[0].name,
                id: value,
              },
            });
          }}
        >
          <Dropdown.Item
            eventKey="0"
            active={filterOptions.Technology.id === "0" }
          >
            Select Techology
          </Dropdown.Item>
          {technologyOptions  == null? null: technologyOptions.map((option) => {
            return (
              <Dropdown.Item
                eventKey={option.id}
                active={
                  filterOptions.Technology.id === option.id
                }
              >
                {option.name}
              </Dropdown.Item>
            );
          })}
        </DropdownButton>
        <Button
          as={ButtonGroup}
          variant="outline-primary"
          className="filter-submit-btn"
          onClick={onFilterSubmit}
        >
          Apply Filter
        </Button>

{
  //Todo: implement the search functionality later
}
        {/* <FormControl
          type="search"
          placeholder="Search"
          className="mr-2"
          aria-label="Search"
          onChange={(e) => {
            setSearchInputValue(e.target.value);
          }}
        /> */}
        {/* <Button variant="outline-dark" onClick={onSearchBtnClicked}>
          <i class="fas fa-search"></i>
        </Button> */}
      </Form>
    </div>
  );
};

export default ProjectsFilterBar;
