#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # CSS to inject
    css_to_add = """
    /* Official Vector SVG Icons */
    .svg-icon {
      width: 15px;
      height: 15px;
      vertical-align: -0.16em;
      display: inline-block;
      flex-shrink: 0;
    }
    .svg-icon-sm {
      width: 13px;
      height: 13px;
      vertical-align: -0.14em;
      display: inline-block;
      flex-shrink: 0;
    }
    .svg-icon-ext {
      width: 12px;
      height: 12px;
      margin-left: 3px;
      vertical-align: -0.1em;
      display: inline-block;
      transition: transform 0.2s ease;
    }
    a:hover .svg-icon-ext, button:hover .svg-icon-ext {
      transform: translate(1.5px, -1.5px);
    }
    .svg-brand-app {
      width: 40px;
      height: 40px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .svg-brand-app svg {
      width: 32px;
      height: 32px;
    }
    .social-badge-icon svg {
      width: 18px;
      height: 18px;
      display: block;
    }
    .triad-compact-icon svg {
      width: 22px;
      height: 22px;
      display: block;
    }
  </style>"""

    if "/* Official Vector SVG Icons */" not in text:
        text = text.replace("  </style>", css_to_add, 1)

    # SVG definitions
    SVG_GITHUB = '<svg class="svg-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>'
    SVG_GITHUB_SM = '<svg class="svg-icon-sm" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>'

    SVG_WECHAT = '<svg class="svg-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8.691 2.188C3.891 2.188 0 5.476 0 9.53c0 2.212 1.17 4.203 3.002 5.55a.59.59 0 0 1 .213.665l-.39 1.48c-.019.07-.048.141-.048.213 0 .163.13.295.29.295a.326.326 0 0 0 .167-.054l1.903-1.114a.864.864 0 0 1 .717-.098 10.16 10.16 0 0 0 2.837.403c.276 0 .543-.027.811-.05-.858-2.554.15-5.253 2.57-6.715 1.99-1.202 4.438-1.455 6.634-.771C17.702 5.6 13.543 2.188 8.691 2.188zm-2.58 3.513c.67 0 1.213.543 1.214 1.214 0 .67-.543 1.214-1.214 1.214a1.214 1.214 0 0 1-1.213-1.214c0-.67.543-1.214 1.213-1.214zm5.162 0c.67 0 1.214.543 1.214 1.214 0 .67-.543 1.214-1.214 1.214a1.214 1.214 0 0 1-1.214-1.214c0-.67.543-1.214 1.214-1.214zM15.308 10.5c-4.14 0-7.5 2.766-7.5 6.18 0 1.865.986 3.545 2.531 4.681a.5.5 0 0 1 .18.562l-.328 1.248c-.016.059-.041.119-.041.18 0 .137.11.248.245.248a.276.276 0 0 0 .141-.046l1.605-.94c.189-.11.4-.15.605-.083a8.56 8.56 0 0 0 2.557.391c4.14 0 7.5-2.767 7.5-6.181 0-3.414-3.36-6.18-7.49-6.18zm-2.176 2.962c.565 0 1.024.459 1.024 1.025 0 .566-.459 1.025-1.024 1.025a1.025 1.025 0 0 1-1.025-1.025c0-.566.46-1.025 1.025-1.025zm4.352 0c.566 0 1.025.459 1.025 1.025 0 .566-.459 1.025-1.025 1.025a1.025 1.025 0 0 1-1.025-1.025c0-.566.459-1.025 1.025-1.025z"/></svg>'
    SVG_WECHAT_SM = SVG_WECHAT.replace('class="svg-icon"', 'class="svg-icon-sm"')

    SVG_MAIL = '<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>'
    SVG_PHONE = '<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
    SVG_EXT = '<svg class="svg-icon-ext" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7"/><path d="M7 7h10v10"/></svg>'

    SVG_APPLE = '<svg viewBox="0 0 170 170" fill="currentColor" aria-hidden="true"><path d="M150.37 130.25c-2.45 5.66-5.35 10.87-8.71 15.66-4.58 6.53-8.33 11.05-11.22 13.56-4.48 4.12-9.28 6.23-14.42 6.35-3.69 0-8.14-1.05-13.32-3.18-5.19-2.12-9.97-3.17-14.34-3.17-4.58 0-9.49 1.05-14.75 3.17-5.26 2.13-9.5 3.24-12.74 3.35-4.35.13-9.16-1.9-14.42-6.08-3.7-3.04-7.59-7.71-11.69-14.01-6.74-10.33-11.77-21.84-15.09-34.54-3.32-12.7-4.98-24.81-4.98-36.33 0-14.15 3.57-26.06 10.7-35.73 7.13-9.67 16.27-14.65 27.42-14.93 4.9 0 10.37 1.34 16.42 4.02 6.05 2.68 9.99 4.07 11.83 4.17 1.63 0 5.8-1.46 12.51-4.38 6.71-2.92 12.39-4.22 17.04-3.9 12.72.63 22.86 5.39 30.43 14.28-11.09 6.75-16.53 16.14-16.32 28.18.22 9.47 3.86 17.38 10.92 23.74 7.06 6.36 15.35 10.02 24.88 10.98-2.17 6.32-4.8 12.55-7.89 18.7zM119.22 31.84c0-7.39 2.66-14.37 7.98-20.94 5.32-6.57 11.96-10.5 19.92-11.79.11 1.09.16 2.07.16 2.94 0 7.39-2.83 14.53-8.49 21.43-5.66 6.9-12.39 10.87-20.19 11.9-.33-1.2-.5-2.2-.5-3.54z"/></svg>'
    SVG_APPLE_SM = f'<span class="svg-icon-sm">{SVG_APPLE}</span>'

    SVG_GOOGLE_PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M3.6 1.7L13.8 12 3.6 22.3c-.4-.4-.6-1-.6-1.7V3.4c0-.7.2-1.3.6-1.7z"/><path fill="#34A853" d="M17.3 8.5L13.8 12l3.5 3.5 4-2.3c1.1-.6 1.1-1.7 0-2.4l-4-2.3z"/><path fill="#EA4335" d="M3.6 22.3l10.2-10.3 3.5 3.5-11.6 6.6c-.8.5-1.7.5-2.1.2z"/><path fill="#FBBC04" d="M3.6 1.7c.4-.3 1.3-.3 2.1.2l11.6 6.6-3.5 3.5L3.6 1.7z"/></svg>'
    SVG_GOOGLE_PLAY_SM = f'<span class="svg-icon-sm">{SVG_GOOGLE_PLAY}</span>'

    SVG_ZOOM = '<svg class="svg-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/><path d="M11 8v6M8 11h6"/></svg>'
    SVG_LOCK = '<svg class="svg-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'
    SVG_IMAGE = '<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>'

    SVG_GRAD = '<svg class="svg-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>'
    SVG_PHONE_SM = '<svg class="svg-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>'
    SVG_PALETTE = '<svg class="svg-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.563-2.512 5.563-5.563C22 6.5 17.5 2 12 2z"/><circle cx="13.5" cy="6.5" r="1" fill="currentColor"/><circle cx="17.5" cy="10.5" r="1" fill="currentColor"/><circle cx="8.5" cy="7.5" r="1" fill="currentColor"/><circle cx="6.5" cy="12.5" r="1" fill="currentColor"/></svg>'
    SVG_BOLT = '<svg class="svg-icon-sm" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'
    SVG_ROCKET = '<svg class="svg-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg>'
    SVG_GLOBE = '<svg class="svg-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>'
    SVG_SPARKLE = '<svg class="svg-icon-sm" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3L12 3z"/></svg>'
    SVG_STAR = '<svg class="svg-icon-sm" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'

    # Social platforms
    SVG_X = '<svg viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>'
    SVG_YOUTUBE = '<svg viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>'
    SVG_QUORA = '<svg viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M12.001 0C5.372 0 0 5.372 0 12c0 6.626 5.372 12 12.001 12 2.457 0 4.74-.741 6.634-2.012l2.671 2.012a.75.75 0 0 0 1.2-.6v-3.79C23.36 17.472 24 14.862 24 12c0-6.628-5.372-12-11.999-12zm4.186 16.71c-.732.55-1.613.93-2.585 1.111l-.85 1.543c-.22.4-.64.636-1.09.636-.2 0-.41-.05-.6-.15a1.26 1.26 0 0 1-.58-1.28l.19-.94c-2.31-.41-4.14-2.35-4.14-4.8 0-2.69 2.21-4.87 4.93-4.87 2.73 0 4.94 2.18 4.94 4.87 0 1.48-.67 2.82-1.73 3.73l1.515.15z"/></svg>'
    SVG_DEVTO = '<svg viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M7.42 10.05c-.18-.1-.4-.14-.66-.14H5.4v4.18h1.36c.26 0 .48-.05.66-.14.18-.1.32-.24.41-.43.1-.19.14-.42.14-.7v-2.07c0-.28-.05-.51-.14-.7-.1-.19-.24-.33-.41-.43v.43zm9.16-.14h-1.32v4.18h1.32v-4.18zm-3.3 0h-1.64v4.18h1.64c.3 0 .56-.06.78-.18.22-.12.38-.3.5-.54.11-.23.17-.52.17-.85v-1.9c0-.33-.06-.61-.17-.85-.11-.24-.28-.42-.5-.54-.22-.11-.48-.17-.78-.17v-.15zm10.72-3.41v15H0v-15h24zm-14.73 4.29H5.4c-.64 0-1.19.22-1.63.66-.45.44-.67.98-.67 1.63v2.96c0 .64.22 1.19.67 1.63.44.44.99.67 1.63.67h3.85c.64 0 1.19-.22 1.64-.67.44-.44.66-.99.66-1.63v-2.96c0-.65-.22-1.19-.66-1.63-.45-.44-.99-.66-1.64-.66h.05zm4.99 7.55h-2.12V6.43h2.12v7.36zm6.36-2.27c0 .64-.22 1.19-.67 1.63-.44.44-.99.67-1.63.67h-3.85c-.65 0-1.19-.22-1.64-.67-.44-.44-.67-.99-.67-1.63v-2.96c0-.65.23-1.19.67-1.63.45-.44.99-.66 1.64-.66h3.85c.64 0 1.19.22 1.63.66.45.44.67.98.67 1.63v2.96z"/></svg>'
    SVG_HASHNODE = '<svg viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M22.351 8.019l-6.37-6.37a5.645 5.645 0 0 0-7.98 0l-6.37 6.37a5.645 5.645 0 0 0 0 7.98l6.37 6.37a5.645 5.645 0 0 0 7.98 0l6.37-6.37a5.645 5.645 0 0 0 0-7.98zm-6.86 4.966a3.491 3.491 0 1 1-4.937-4.937 3.491 3.491 0 0 1 4.937 4.937z"/></svg>'
    SVG_PRODUCTHUNT = '<svg viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm0 18.5c-.828 0-1.5-.672-1.5-1.5v-3.5H9.25c-.414 0-.75-.336-.75-.75V7.75c0-.414.336-.75.75-.75h4.25c2.485 0 4.5 2.015 4.5 4.5s-2.015 4.5-4.5 4.5H12v2.5zm0-8.5h1.5c.828 0 1.5-.672 1.5-1.5s-.672-1.5-1.5-1.5H12v3z"/></svg>'
    SVG_HACKERNEWS = '<svg viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M0 0v24h24V0H0zm12.923 13.91v4.887h-1.846v-4.887L7.42 5.203h2.128l2.427 4.887 2.427-4.887h2.128l-3.607 8.707z"/></svg>'
    SVG_MEDIUM = '<svg viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M13.54 12a6.8 6.8 0 0 1-6.77 6.82A6.8 6.8 0 0 1 0 12a6.8 6.8 0 0 1 6.77-6.82A6.8 6.8 0 0 1 13.54 12zm7.42 0c0 3.54-1.51 6.42-3.38 6.42-1.87 0-3.39-2.88-3.39-6.42s1.52-6.42 3.39-6.42 3.38 2.88 3.38 6.42M24 12c0 3.17-.53 5.75-1.19 5.75-.66 0-1.19-2.58-1.19-5.75s.53-5.75 1.19-5.75C23.47 6.25 24 8.83 24 12z"/></svg>'

    # Modal close, back-to-top
    SVG_CLOSE = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
    SVG_ARROW_UP = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 5 19 12"/></svg>'

    # Triad icons
    SVG_WAVE = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12c3-6 7-6 10 0s7 6 10 0"/></svg>'
    SVG_CRAFT = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>'
    SVG_DIAMOND = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 22 12 12 22 2 12 12 2"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="8" y1="12" x2="16" y2="12"/></svg>'

    replacements = [
        # Hero CTA
        ('🐙 GitHub @kristen7416', f'{SVG_GITHUB} GitHub @kristen7416'),
        # Hero Tags
        ('<span class="dense-tag highlight">🎓 211 金融数学</span>', f'<span class="dense-tag highlight">{SVG_GRAD} 211 金融数学</span>'),
        ('<span class="dense-tag">📱 微信公众号图文采编排版 (秀米/135)</span>', f'<span class="dense-tag">{SVG_PHONE_SM} 微信公众号图文采编排版 (秀米/135)</span>'),
        ('<span class="dense-tag">🎨 晚会入场券/书签印刷打样</span>', f'<span class="dense-tag">{SVG_PALETTE} 晚会入场券/书签印刷打样</span>'),
        ('<span class="dense-tag">🍏 App Store 2560x1600 高清图</span>', f'<span class="dense-tag">{SVG_APPLE_SM} App Store 2560x1600 高清图</span>'),
        ('<span class="dense-tag">⚡ GitHub 842 次贡献 (69 PR 合并)</span>', f'<span class="dense-tag">{SVG_BOLT} GitHub 842 次贡献 (69 PR 合并)</span>'),
        ('<span class="dense-tag">🚀 3 款全栈上线交付产品</span>', f'<span class="dense-tag">{SVG_ROCKET} 3 款全栈上线交付产品</span>'),
        # Hero Contacts
        ('📧 kristen6670@163.com', f'{SVG_MAIL} kristen6670@163.com'),
        ('💬 微信: kristen6670', f'{SVG_WECHAT} 微信: kristen6670'),
        ('📞 18708165973', f'{SVG_PHONE} 18708165973'),
        ('🐙 github.com/kristen7416', f'{SVG_GITHUB} github.com/kristen7416'),
        # Hero Triad
        ('<div class="triad-compact-icon">∿</div>', f'<div class="triad-compact-icon">{SVG_WAVE}</div>'),
        ('<div class="triad-compact-icon">☼</div>', f'<div class="triad-compact-icon">{SVG_CRAFT}</div>'),
        ('<div class="triad-compact-icon">❖</div>', f'<div class="triad-compact-icon">{SVG_DIAMOND}</div>'),
        # Section 1
        ('<span class="status-pill sage">✨ 真实已发表案例</span>', f'<span class="status-pill sage">{SVG_SPARKLE} 真实已发表案例</span>'),
        ('🔗 跳转微信阅读原文 ↗', f'{SVG_WECHAT_SM} 跳转微信阅读原文 {SVG_EXT}'),
        # Section 2
        ('🔍 点击放大全图', f'{SVG_ZOOM} 点击放大全图'),
        ('<div style="font-size: 2.2rem;">🍏</div>', f'<div class="svg-brand-app" style="color: var(--color-charcoal);">{SVG_APPLE}</div>'),
        ('🔗 访问 iOS App Store 页面 ↗', f'{SVG_APPLE_SM} 访问 iOS App Store 页面 {SVG_EXT}'),
        ('<div style="font-size: 2.2rem;">🤖</div>', f'<div class="svg-brand-app">{SVG_GOOGLE_PLAY}</div>'),
        ('🔗 访问 Google Play 页面 ↗', f'{SVG_GOOGLE_PLAY_SM} 访问 Google Play 页面 {SVG_EXT}'),
        ('🖼️ LynavoDrive 官方应用商店全景展览图（App Store Panoramic Showcase）', f'{SVG_IMAGE} LynavoDrive 官方应用商店全景展览图（App Store Panoramic Showcase）'),
        ('🔍 点击全屏查看高清展览图', f'{SVG_ZOOM} 点击全屏查看高清展览图'),
        ('🔒 apps.apple.com/app/lynavodrive · App Store 官方上架全景展览图', f'{SVG_LOCK} apps.apple.com/app/lynavodrive · App Store 官方上架全景展览图'),
        ('📱 单张高清详细分图（01 ~ 06 · 2560x1600 · 点击放大）', f'{SVG_PHONE_SM} 单张高清详细分图（01 ~ 06 · 2560x1600 · 点击放大）'),
        # Section 3
        ('<span class="status-pill sage">🟢 GitHub 842 Contributions</span>', f'<span class="status-pill sage">{SVG_GITHUB_SM} 842 Contributions</span>'),
        ('🔒 github.com/kristen7416', f'{SVG_LOCK} github.com/kristen7416'),
        ('🐙 访问 GitHub 主页 (@kristen7416) ↗', f'{SVG_GITHUB_SM} 访问 GitHub 主页 (@kristen7416) {SVG_EXT}'),
        ('🚀 立即在线访问 ↗', f'{SVG_ROCKET} 立即在线访问 {SVG_EXT}'),
        ('🌐 访问产品官网 ↗', f'{SVG_GLOBE} 访问产品官网 {SVG_EXT}'),
        ('🚀 在线交互体验 ↗', f'{SVG_ROCKET} 在线交互体验 {SVG_EXT}'),
        ('🐙 源码仓库', f'{SVG_GITHUB_SM} 源码仓库'),
        # Section 4
        ('<span class="status-pill sky">🌐 全球社媒矩阵</span>', f'<span class="status-pill sky">{SVG_GLOBE} 全球社媒矩阵</span>'),
        ('<div class="social-badge-icon" style="background: #000000;">𝕏</div>', f'<div class="social-badge-icon" style="background: #000000;">{SVG_X}</div>'),
        ('<div class="social-badge-icon" style="background: #E62117;">▶</div>', f'<div class="social-badge-icon" style="background: #FF0000;">{SVG_YOUTUBE}</div>'),
        ('<div class="social-badge-icon" style="background: #B92B27;">Q</div>', f'<div class="social-badge-icon" style="background: #B92B27;">{SVG_QUORA}</div>'),
        ('<div class="social-badge-icon" style="background: #0A0A0A;">DEV</div>', f'<div class="social-badge-icon" style="background: #0A0A0A;">{SVG_DEVTO}</div>'),
        ('<div class="social-badge-icon" style="background: #2962FF;">H</div>', f'<div class="social-badge-icon" style="background: #2962FF;">{SVG_HASHNODE}</div>'),
        ('<div class="social-badge-icon" style="background: #DA552F;">P</div>', f'<div class="social-badge-icon" style="background: #DA552F;">{SVG_PRODUCTHUNT}</div>'),
        ('<div class="social-badge-icon" style="background: #FF6600;">Y</div>', f'<div class="social-badge-icon" style="background: #FF6600;">{SVG_HACKERNEWS}</div>'),
        ('<div class="social-badge-icon" style="background: #12100E;">M</div>', f'<div class="social-badge-icon" style="background: #12100E;">{SVG_MEDIUM}</div>'),
        ('查看 X 推文 ↗', f'查看 X 推文 {SVG_EXT}'),
        ('观看 YouTube 视频 ↗', f'观看 YouTube 视频 {SVG_EXT}'),
        ('阅读 Quora 回答 ↗', f'阅读 Quora 回答 {SVG_EXT}'),
        ('访问 Dev.to 文章 ↗', f'访问 Dev.to 文章 {SVG_EXT}'),
        ('阅读 Hashnode 文章 ↗', f'阅读 Hashnode 文章 {SVG_EXT}'),
        ('查看 PH 讨论帖 ↗', f'查看 PH 讨论帖 {SVG_EXT}'),
        ('查看 HN 帖子 ↗', f'查看 HN 帖子 {SVG_EXT}'),
        ('阅读 Medium 母文 ↗', f'阅读 Medium 母文 {SVG_EXT}'),
        ('<span>⚡ 支撑底层：AI Agent 辅助运营流水线架构</span>', f'<span>{SVG_BOLT} 支撑底层：AI Agent 辅助运营流水线架构</span>'),
        ('🌟 延伸视觉创作：科技产品 Medium 深度长文头图', f'{SVG_STAR} 延伸视觉创作：科技产品 Medium 深度长文头图'),
        ('查看 Medium 原文 ↗', f'查看 Medium 原文 {SVG_EXT}'),
        ('🔍 点击放大头图', f'{SVG_ZOOM} 点击放大头图'),
        # Modal, Toast, Back to top
        ('<button class="lightbox-close-btn" onclick="closeModal()" aria-label="关闭预览">✕</button>', f'<button class="lightbox-close-btn" onclick="closeModal()" aria-label="关闭预览">{SVG_CLOSE}</button>'),
        ('<span id="toastIcon">✨</span>', f'<span id="toastIcon">{SVG_SPARKLE}</span>'),
        ('<button class="back-to-top-btn" id="backToTopBtn" onclick="window.scrollTo({top: 0, behavior: \'smooth\'})" aria-label="返回顶部">↑</button>', f'<button class="back-to-top-btn" id="backToTopBtn" onclick="window.scrollTo({{top: 0, behavior: \'smooth\'}})" aria-label="返回顶部">{SVG_ARROW_UP}</button>')
    ]

    for old, new in replacements:
        if old not in text:
            print(f"Warning: NOT FOUND: {old[:50]}")
        text = text.replace(old, new)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)

    print("Success: all vector SVG icons applied cleanly to index.html!")

if __name__ == '__main__':
    main()
