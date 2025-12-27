import { GRID_WIDTH, GRID_HEIGHT, EntityType, Direction, ResourceType, SPAWN_INTERVAL } from './constants.js';

/**
 * Represents the game world - a grid of cells containing entities.
 *
 * Agentic Coding Parallel:
 * - The grid is like your "agent topology" - where can data flow?
 * - Each cell is a potential agent or connection point
 * - Empty cells = no pipeline exists there
 */
export class World {
    constructor() {
        // 2D grid of cells
        this.grid = this.createEmptyGrid();

        // Items currently moving through the world
        this.items = [];

        // Statistics
        this.itemsCollected = 0;
        this.recentCollections = []; // timestamps for throughput calc

        // Initialize with some starting entities
        this.setupInitialWorld();
    }

    createEmptyGrid() {
        const grid = [];
        for (let y = 0; y < GRID_HEIGHT; y++) {
            const row = [];
            for (let x = 0; x < GRID_WIDTH; x++) {
                row.push({ type: EntityType.EMPTY });
            }
            grid.push(row);
        }
        return grid;
    }

    setupInitialWorld() {
        // Place an iron node on the left
        this.setCell(2, 7, {
            type: EntityType.NODE,
            resource: ResourceType.IRON,
            lastSpawn: 0
        });

        // Place a copper node on the top
        this.setCell(10, 2, {
            type: EntityType.NODE,
            resource: ResourceType.COPPER,
            lastSpawn: 0
        });

        // Place a chest on the right
        this.setCell(17, 7, {
            type: EntityType.CHEST
        });

        // Place another chest at bottom
        this.setCell(10, 12, {
            type: EntityType.CHEST
        });
    }

    getCell(x, y) {
        if (x < 0 || x >= GRID_WIDTH || y < 0 || y >= GRID_HEIGHT) {
            return null;
        }
        return this.grid[y][x];
    }

    setCell(x, y, entity) {
        if (x >= 0 && x < GRID_WIDTH && y >= 0 && y < GRID_HEIGHT) {
            this.grid[y][x] = entity;
        }
    }

    /**
     * Place a belt at the given grid position
     */
    placeBelt(x, y, direction) {
        const cell = this.getCell(x, y);
        if (cell && cell.type === EntityType.EMPTY) {
            this.setCell(x, y, {
                type: EntityType.BELT,
                direction: direction
            });
            return true;
        }
        return false;
    }

    /**
     * Remove an entity (but not nodes/chests)
     */
    deleteEntity(x, y) {
        const cell = this.getCell(x, y);
        if (cell && cell.type === EntityType.BELT) {
            this.setCell(x, y, { type: EntityType.EMPTY });
            return true;
        }
        return false;
    }

    /**
     * Spawn items from resource nodes
     */
    spawnItems(timestamp) {
        for (let y = 0; y < GRID_HEIGHT; y++) {
            for (let x = 0; x < GRID_WIDTH; x++) {
                const cell = this.getCell(x, y);
                if (cell.type === EntityType.NODE) {
                    if (timestamp - cell.lastSpawn >= SPAWN_INTERVAL) {
                        // Spawn a new item at the node's position
                        this.items.push({
                            x: x,
                            y: y,
                            pixelX: x * 40 + 20, // center of cell
                            pixelY: y * 40 + 20,
                            resource: cell.resource
                        });
                        cell.lastSpawn = timestamp;
                    }
                }
            }
        }
    }

    /**
     * Calculate throughput (items per second over last 5 seconds)
     */
    getThroughput(timestamp) {
        const fiveSecondsAgo = timestamp - 5000;
        this.recentCollections = this.recentCollections.filter(t => t > fiveSecondsAgo);
        return (this.recentCollections.length / 5).toFixed(1);
    }

    /**
     * Record that an item was collected
     */
    collectItem(timestamp) {
        this.itemsCollected++;
        this.recentCollections.push(timestamp);
    }
}
