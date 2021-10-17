import {
  Form,
  FormControl,
  Button,
  Dropdown,
  DropdownButton,
  ButtonGroup,
} from "react-bootstrap";

const ProjectsFilterBar = ({
  filterOptions,
  setFilterOptions,
  onFilterSubmit,
  setSearchInputValue,
  onSearchBtnClicked,
}) => {
  //Todo: send request to the back end api to fetch all data
  const serviceOptions = [
    {
      name: "IOS app development",
      key: "312",
    },
    {
      name: "Android app development",
      key: "3889",
    },
    {
      name: "Cross-Platform Desktop app development",
      key: "984",
    },
    {
      name: "Front-end web development",
      key: "4378",
    },
    {
      name: "Back-end web development",
      key: "4983",
    },
    {
      name: "Game development",
      key: "1328",
    },
  ];
  const platformOptions = [
    {
      name: "iOS",
      key: "3453",
    },
    {
      name: "Android",
      key: "3498",
    },
    {
      name: "Windows",
      key: "4938",
    },
    {
      name: "macOS",
      key: "3498e",
    },
    {
      name: "Linux",
      key: "23r34",
    },
    {
      name: "Web",
      key: "4etr434",
    },
  ];
  const technologyOptions = [
    {
      name: "Python Flask",
      key: "eoiwu323",
    },
    {
      name: "Flutter",
      key: "34532re3",
    },
    {
      name: "ReactJS",
      key: "ieuwouie90",
    },
    {
      name: "Node.JS",
      key: "434r34r34",
    },
    {
      name: "Unity 3D",
      key: "4983",
    },
    {
      name: "jQuery",
      key: "34534r34",
    },
  ];

  return (
    <div className="filter-bar">
      <Form>
        <DropdownButton
          as={ButtonGroup}
          key="Service"
          id="dropdown-variants-Service"
          variant="outline-dark"
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
                        return option.key === value ? option.name : null;
                      })[0].name,
                key: value,
              },
            });
          }}
        >
          <Dropdown.Item
            eventKey="0"
            active={filterOptions.Service.key === "0" ? true : false}
          >
            Select Service
          </Dropdown.Item>
          {serviceOptions.map((option) => {
            return (
              <Dropdown.Item
                eventKey={option.key}
                active={filterOptions.Service.key === option.key ? true : false}
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
                        return option.key === value ? option.name : null;
                      })[0].name,
                key: value,
              },
            });
          }}
        >
          <Dropdown.Item
            eventKey="0"
            active={filterOptions.Platform.key === "0" ? true : false}
          >
            Select Platform
          </Dropdown.Item>
          {platformOptions.map((option) => {
            return (
              <Dropdown.Item
                eventKey={option.key}
                active={
                  filterOptions.Platform.key === option.key ? true : false
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
                        return option.key === value ? option.name : null;
                      })[0].name,
                key: value,
              },
            });
          }}
        >
          <Dropdown.Item
            eventKey="0"
            active={filterOptions.Technology.key === "0" ? true : false}
          >
            Select Techology
          </Dropdown.Item>
          {technologyOptions.map((option) => {
            return (
              <Dropdown.Item
                eventKey={option.key}
                active={
                  filterOptions.Technology.key === option.key ? true : false
                }
              >
                {option.name}
              </Dropdown.Item>
            );
          })}
        </DropdownButton>
        <Button
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
        <Button variant="outline-dark" onClick={onSearchBtnClicked}>
          <i class="fas fa-search"></i>
        </Button>
      </Form>
    </div>
  );
};

export default ProjectsFilterBar;
