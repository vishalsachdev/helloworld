import { CELL_SIZE, GRID_WIDTH, GRID_HEIGHT, EntityType, Direction, Colors, ResourceType } from './constants.js';

/**
 * Handles all canvas rendering.
 *
 * Agentic Coding Parallel:
 * - Visualization is crucial for debugging agent flows
 * - Seeing items move helps you understand throughput
 * - This is like adding observability to your agent pipeline
 */
export class Renderer {
    constructor(canvas) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
    }

    clear() {
        this.ctx.fillStyle = '#0f0f1a';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    }

    drawGrid() {
        this.ctx.strokeStyle = Colors.GRID_LINE;
        this.ctx.lineWidth = 1;

        // Vertical lines
        for (let x = 0; x <= GRID_WIDTH; x++) {
            this.ctx.beginPath();
            this.ctx.moveTo(x * CELL_SIZE, 0);
            this.ctx.lineTo(x * CELL_SIZE, GRID_HEIGHT * CELL_SIZE);
            this.ctx.stroke();
        }

        // Horizontal lines
        for (let y = 0; y <= GRID_HEIGHT; y++) {
            this.ctx.beginPath();
            this.ctx.moveTo(0, y * CELL_SIZE);
            this.ctx.lineTo(GRID_WIDTH * CELL_SIZE, y * CELL_SIZE);
            this.ctx.stroke();
        }
    }

    drawWorld(world) {
        for (let y = 0; y < GRID_HEIGHT; y++) {
            for (let x = 0; x < GRID_WIDTH; x++) {
                const cell = world.getCell(x, y);
                this.drawCell(x, y, cell);
            }
        }
    }

    drawCell(x, y, cell) {
        const px = x * CELL_SIZE;
        const py = y * CELL_SIZE;
        const centerX = px + CELL_SIZE / 2;
        const centerY = py + CELL_SIZE / 2;

        switch (cell.type) {
            case EntityType.BELT:
                this.drawBelt(px, py, cell.direction);
                break;

            case EntityType.NODE:
                this.drawNode(px, py, cell.resource);
                break;

            case EntityType.CHEST:
                this.drawChest(px, py);
                break;
        }
    }

    drawBelt(px, py, direction) {
        // Belt background
        this.ctx.fillStyle = Colors.BELT;
        this.ctx.fillRect(px + 2, py + 2, CELL_SIZE - 4, CELL_SIZE - 4);

        // Direction arrow
        const centerX = px + CELL_SIZE / 2;
        const centerY = py + CELL_SIZE / 2;
        const arrowSize = 10;

        this.ctx.save();
        this.ctx.translate(centerX, centerY);
        this.ctx.rotate((direction * Math.PI) / 2);

        this.ctx.fillStyle = Colors.BELT_ARROW;
        this.ctx.beginPath();
        this.ctx.moveTo(arrowSize, 0);
        this.ctx.lineTo(-arrowSize / 2, -arrowSize / 2);
        this.ctx.lineTo(-arrowSize / 2, arrowSize / 2);
        this.ctx.closePath();
        this.ctx.fill();

        this.ctx.restore();
    }

    drawNode(px, py, resource) {
        const color = resource === ResourceType.IRON ? Colors.NODE_IRON : Colors.NODE_COPPER;
        const label = resource === ResourceType.IRON ? 'Fe' : 'Cu';

        // Outer glow
        this.ctx.fillStyle = color + '40';
        this.ctx.fillRect(px, py, CELL_SIZE, CELL_SIZE);

        // Inner square
        this.ctx.fillStyle = color;
        this.ctx.fillRect(px + 5, py + 5, CELL_SIZE - 10, CELL_SIZE - 10);

        // Label
        this.ctx.fillStyle = '#000';
        this.ctx.font = 'bold 14px monospace';
        this.ctx.textAlign = 'center';
        this.ctx.textBaseline = 'middle';
        this.ctx.fillText(label, px + CELL_SIZE / 2, py + CELL_SIZE / 2);
    }

    drawChest(px, py) {
        // Chest background
        this.ctx.fillStyle = Colors.CHEST;
        this.ctx.fillRect(px + 3, py + 3, CELL_SIZE - 6, CELL_SIZE - 6);

        // Chest icon
        this.ctx.fillStyle = '#fff';
        this.ctx.font = '20px sans-serif';
        this.ctx.textAlign = 'center';
        this.ctx.textBaseline = 'middle';
        this.ctx.fillText('📦', px + CELL_SIZE / 2, py + CELL_SIZE / 2);
    }

    drawItems(items) {
        for (const item of items) {
            const color = item.resource === ResourceType.IRON ?
                Colors.ITEM_IRON : Colors.ITEM_COPPER;

            // Draw item as a small circle
            this.ctx.fillStyle = color;
            this.ctx.beginPath();
            this.ctx.arc(item.pixelX, item.pixelY, 6, 0, Math.PI * 2);
            this.ctx.fill();

            // Add a subtle border
            this.ctx.strokeStyle = '#000';
            this.ctx.lineWidth = 1;
            this.ctx.stroke();
        }
    }

    drawPlacementPreview(gridX, gridY, direction, canPlace) {
        const px = gridX * CELL_SIZE;
        const py = gridY * CELL_SIZE;

        // Semi-transparent preview
        this.ctx.globalAlpha = 0.5;

        if (canPlace) {
            this.drawBelt(px, py, direction);
        } else {
            // Red overlay for invalid placement
            this.ctx.fillStyle = '#ff000040';
            this.ctx.fillRect(px, py, CELL_SIZE, CELL_SIZE);
        }

        this.ctx.globalAlpha = 1.0;
    }

    render(world, mouseGridX, mouseGridY, currentDirection, currentTool) {
        this.clear();
        this.drawGrid();
        this.drawWorld(world);
        this.drawItems(world.items);

        // Show placement preview when hovering
        if (currentTool === 'belt' && mouseGridX >= 0 && mouseGridY >= 0) {
            const cell = world.getCell(mouseGridX, mouseGridY);
            const canPlace = cell && cell.type === EntityType.EMPTY;
            this.drawPlacementPreview(mouseGridX, mouseGridY, currentDirection, canPlace);
        }
    }
}
