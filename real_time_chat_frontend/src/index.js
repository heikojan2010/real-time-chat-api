import React from 'react';
import ReactDOM from 'react-dom';
import './index.scss';
import App from './Chatapp';


/**
 * Maintain a simple map of React components to make it easier
 * for Django to reference individual components
 */
const pages = {
    App,
}

/**
 * If Django hasn't injected these properties into the HTML
 * template that's loading this script then we're viewing it
 * via the create-react-app liveserver
 */
window.component = window.component || 'App';
window.props = window.props || { env: 'Create-React-App' };
window.reactRoot = window.reactRoot || document.getElementById('root');

/**
 * React the component as usual
 */
ReactDOM.render(
    React.createElement(pages[window.component], window.props),
    window.reactRoot,
);