from config import Config
from models.llm_interface import get_model
from core.tree_manager import TreeManager
import tasks

if __name__ == '__main__':
    cfg = Config()
    model = get_model(cfg)
    prompt = tasks.get_prompt(cfg.task)
    tm = TreeManager(model, max_depth=cfg.max_depth, beam_width=cfg.beam_width)
    best = tm.solve(prompt)
    print("Best Thought Path:\n", best.text)
