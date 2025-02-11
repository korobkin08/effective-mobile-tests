from playwright.sync_api import TimeoutError

def wait_for(page, condition, timeout=15000):
    try:
        if isinstance(condition, str):
            page.wait_for_load_state(condition, timeout=timeout)
        else:
            page.wait_for_function(condition, timeout=timeout)
    except TimeoutError:
        raise AssertionError(f"Timeout waiting for {condition}")