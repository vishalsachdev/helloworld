// Grid and cell dimensions
export const CELL_SIZE = 40;
export const GRID_WIDTH = 20;  // cells
export const GRID_HEIGHT = 15; // cells

// Directions (clockwise from right)
export const Direction = {
    RIGHT: 0,
    DOWN: 1,
    LEFT: 2,
    UP: 3
};

// Direction vectors for movement
export const DIR_VECTORS = {
    [Direction.RIGHT]: { x: 1, y: 0 },
    [Direction.DOWN]: { x: 0, y: 1 },
    [Direction.LEFT]: { x: -1, y: 0 },
    [Direction.UP]: { x: 0, y: -1 }
};

// Entity types
export const EntityType = {
    EMPTY: 'empty',
    BELT: 'belt',
    NODE: 'node',
    CHEST: 'chest'
};

// Resource types (for future expansion)
export const ResourceType = {
    IRON: 'iron',
    COPPER: 'copper'
};

// Colors
export const Colors = {
    GRID_LINE: '#1a2a3a',
    BELT: '#3a3a5a',
    BELT_ARROW: '#666',
    NODE_IRON: '#a0a0c0',
    NODE_COPPER: '#c08040',
    CHEST: '#4a6a4a',
    ITEM_IRON: '#c0c0e0',
    ITEM_COPPER: '#e0a060'
};

// Game speed
export const ITEM_SPEED = 2;           // pixels per frame
export const SPAWN_INTERVAL = 1000;    // ms between item spawns
