import React from "react";
import Category from "./Category";

var $ = require("jquery");

export default class CategoryPane extends React.Component {
    constructor(props) {
        super(props);
        this.state = {category_arr: []};
    }

    componentDidMount() {
        this.getCategories();
    }

    getCategories() {
        return $.getJSON(window.location.href + 'get_categories', (data) => {
            console.log(data);
            this.setState({category_arr: data});
        });
    }

    render () {
        return (
            <div className="category-pane">
                {this.state.category_arr.map((value, index) => {
                    return <Category name={value} key={index} />
                })}
            </div>
        );
    }
}
