import React from "react";
import Header from "./Header"
import CategoryPane from "./CategoryPane"

export default class App extends React.Component {
    render () {
        return (
            <div className="component-app">
                <Header />
                <CategoryPane />
            </div>
        );
    }
}
