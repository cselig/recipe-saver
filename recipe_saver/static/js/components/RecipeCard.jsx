import React from "react";

export default class RecipeCard extends React.Component {
    render() {
        return (
            <p>{this.props.name}</p>
        )
    }
}
