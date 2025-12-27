import { CELL_SIZE, GRID_WIDTH, GRID_HEIGHT, Direction, DIR_VECTORS, EntityType, ITEM_SPEED } from './constants.js';
import { World } from './world.js';
import { Renderer } from './renderer.js';

/**
 * Main game controller.
 *
 * This is the "orchestrator" - like the top-level agent that coordinates
 * all the specialized agents (world, renderer, input handling).
 */
class Game {
    constructor() {
        this.canvas = document.getElementById('game-canvas');
        this.world = new World();
        this.renderer = new Renderer(this.canvas);

        // Current tool and direction
        this.currentTool = 'belt';
        this.currentDirection = Direction.RIGHT;

        // Mouse state
        this.mouseGridX = -1;
        this.mouseGridY = -1;

        // UI elements
        this.itemsCollectedEl = document.getElementById('items-collected');
        this.throughputEl = document.getElementById('throughput');

        this.setupEventListeners();
        this.lastTimestamp = 0;

        // Start game loop
        requestAnimationFrame((t) => this.gameLoop(t));
    }

    setupEventListeners() {
        // Mouse movement for preview
        this.canvas.addEventListener('mousemove', (e) => {
            const rect = this.canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            this.mouseGridX = Math.floor(x / CELL_SIZE);
            this.mouseGridY = Math.floor(y / CELL_SIZE);
        });

        // Mouse leave
        this.canvas.addEventListener('mouseleave', () => {
            this.mouseGridX = -1;
            this.mouseGridY = -1;
        });

        // Click to place/delete
        this.canvas.addEventListener('click', () => {
            if (this.mouseGridX < 0 || this.mouseGridY < 0) return;

            if (this.currentTool === 'belt') {
                this.world.placeBelt(this.mouseGridX, this.mouseGridY, this.currentDirection);
            } else if (this.currentTool === 'delete') {
                this.world.deleteEntity(this.mouseGridX, this.mouseGridY);
            }
        });

        // Keyboard for rotation
        document.addEventListener('keydown', (e) => {
            if (e.key === 'r' || e.key === 'R') {
                // Rotate clockwise
                this.currentDirection = (this.currentDirection + 1) % 4;
            }
        });

        // Tool buttons
        document.querySelectorAll('.tool-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.tool-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                this.currentTool = btn.dataset.tool;
            });
        });
    }

    /**
     * Main game loop - runs every frame (~60fps)
     */
    gameLoop(timestamp) {
        // Spawn new items from nodes
        this.world.spawnItems(timestamp);

        // Move items along belts
        this.moveItems(timestamp);

        // Check for items reaching chests
        this.collectItems(timestamp);

        // Render everything
        this.renderer.render(
            this.world,
            this.mouseGridX,
            this.mouseGridY,
            this.currentDirection,
            this.currentTool
        );

        // Update UI stats
        this.itemsCollectedEl.textContent = this.world.itemsCollected;
        this.throughputEl.textContent = this.world.getThroughput(timestamp);

        this.lastTimestamp = timestamp;
        requestAnimationFrame((t) => this.gameLoop(t));
    }

    /**
     * Move items along conveyor belts.
     *
     * THIS IS THE CORE FLOW LOGIC - the most important function in the game!
     *
     * For each item:
     * 1. Find what cell it's currently in
     * 2. If it's on a belt, move it in the belt's direction
     * 3. Handle transitions between cells
     *
     * TODO: Implement this function!
     *
     * Agentic Coding Parallel:
     * - Each item is like a "message" or "context" flowing between agents
     * - The belt direction determines which agent receives the data next
     * - Items can only move where belts exist (like defined pipelines)
     */
    moveItems(timestamp) {
        // TODO: Your implementation here!
        //
        // Hints:
        // - Loop through this.world.items
        // - For each item, find its grid position: Math.floor(item.pixelX / CELL_SIZE)
        // - Get the cell at that position: this.world.getCell(gridX, gridY)
        // - If it's a belt, use DIR_VECTORS[cell.direction] to get movement
        // - Update item.pixelX and item.pixelY by ITEM_SPEED * direction
        // - Handle cell boundaries (when item moves to next cell)
        //
        // Think about:
        // - What happens when an item reaches the edge of a belt?
        // - What if the next cell isn't a belt?
        // - How do you know when an item has "arrived" at its destination cell?

        for (const item of this.world.items) {
            // Find current grid position
            const gridX = Math.floor(item.pixelX / CELL_SIZE);
            const gridY = Math.floor(item.pixelY / CELL_SIZE);
            const cell = this.world.getCell(gridX, gridY);

            // Only move if on a belt
            if (cell && cell.type === EntityType.BELT) {
                const dir = DIR_VECTORS[cell.direction];
                item.pixelX += dir.x * ITEM_SPEED;
                item.pixelY += dir.y * ITEM_SPEED;
            }
        }
    }

    /**
     * Check if items have reached chests and collect them.
     */
    collectItems(timestamp) {
        this.world.items = this.world.items.filter(item => {
            const gridX = Math.floor(item.pixelX / CELL_SIZE);
            const gridY = Math.floor(item.pixelY / CELL_SIZE);
            const cell = this.world.getCell(gridX, gridY);

            if (cell && cell.type === EntityType.CHEST) {
                // Item collected!
                this.world.collectItem(timestamp);
                return false; // Remove from items array
            }

            // Also remove items that went off-grid
            if (gridX < 0 || gridX >= GRID_WIDTH || gridY < 0 || gridY >= GRID_HEIGHT) {
                return false;
            }

            return true; // Keep item
        });
    }
}

// Start the game when page loads
window.addEventListener('DOMContentLoaded', () => {
    new Game();
});
