# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 09:15:46

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 278
- **总 Thread 数**: 31
- **大型 Thread** (>20封): 3 个

### 分类分布

- **PATCH**: 27 threads (233 邮件)
- **Bug Report**: 1 threads (1 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Other**: 2 threads (42 邮件)

---

## 📌 PATCH

共 27 个 thread

---

### Thread 1: [PATCH v4 00/43] KVM: arm64: Revamp Fine Grained Trap handling

**📧 邮件数**: 47 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  6 May 2025 17:43:05 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是对 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的细粒度陷阱（Fine Grained Trap，FGT）处理的改进，特别是针对 FEAT_FGT2 特性的补充和优化。

1. **原始 patch/问题的内容**：
   本次讨论的补丁系列（PATCH v4 00/43）旨在重构 KVM 对细粒度陷阱的处理，特别是引入 FEAT_FGT2 特性，增加对新寄存器的支持，并改进现有寄存器的处理逻辑。

2. **之前讨论要点**：
   在之前的讨论中，Marc Zyngier 提到该补丁系列的规模大幅增加，主要是由于添加了对 FEAT_FGT2 的全面支持和相关寄存器的描述。此外，补丁中还修复了多处注释中的错误，并清理了代码中的冗余部分。

3. **本周的新讨论、进展或结论**：
   本周的讨论集中在对 FEAT_FGT2 寄存器的处理上，包括：
   - 增加了对 FEAT_FGT2 寄存器的描述和陷阱路由。
   - 通过表驱动的方式配置 FGU（Fine Grained Unit）行为，简化了代码的维护。
   - 引入了新的功能映射，确保在处理寄存器时能够正确计算 RES0 状态。
   - 讨论了如何在 KVM 中实现对 FEAT_FGT2 寄存器的上下文切换，确保主机配置不会泄漏到客户机中。
   - 进行了多次代码审查和优化，确保补丁的逻辑清晰且符合架构要求。

总的来说，本周的讨论和补丁提交为 KVM 在 ARM64 下的细粒度陷阱处理提供了重要的进展，增强了对新特性的支持，并提高了代码的可读性和可维护性。

#### 📝 邮件列表

1. **[05-06 17:43]** [PATCH v4 00/43] KVM: arm64: Revamp Fine Grained Trap handling
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[05-06 17:43]** [PATCH v4 01/43] arm64: sysreg: Add ID_AA64ISAR1_EL1.LS64 encoding for FEAT_LS64WB
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[05-06 17:43]** [PATCH v4 02/43] arm64: sysreg: Update ID_AA64MMFR4_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[05-06 17:43]** [PATCH v4 03/43] arm64: sysreg: Add layout for HCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[05-06 17:43]** [PATCH v4 04/43] arm64: sysreg: Replace HFGxTR_EL2 with HFG{R,W}TR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[05-06 17:43]** [PATCH v4 05/43] arm64: sysreg: Update ID_AA64PFR0_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[05-06 17:43]** [PATCH v4 06/43] arm64: sysreg: Update PMSIDR_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[05-06 17:43]** [PATCH v4 07/43] arm64: sysreg: Update TRBIDR_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[05-06 17:43]** [PATCH v4 08/43] arm64: sysreg: Update CPACR_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[05-06 17:43]** [PATCH v4 09/43] arm64: sysreg: Add registers trapped by HFG{R,W}TR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[05-06 17:43]** [PATCH v4 10/43] arm64: sysreg: Add registers trapped by HDFG{R,W}TR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[05-06 17:43]** [PATCH v4 11/43] arm64: sysreg: Add system instructions trapped by HFGIRT2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[05-06 17:43]** [PATCH v4 12/43] arm64: Remove duplicated sysreg encodings
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[05-06 17:43]** [PATCH v4 13/43] arm64: tools: Resync sysreg.h
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[05-06 17:43]** [PATCH v4 14/43] arm64: Add syndrome information for trapped LD64B/ST64B{,V,V0}
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[05-06 17:43]** [PATCH v4 15/43] arm64: Add FEAT_FGT2 capability
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[05-06 17:43]** [PATCH v4 16/43] KVM: arm64: Tighten handling of unknown FGT groups
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[05-06 17:43]** [PATCH v4 17/43] KVM: arm64: Simplify handling of negative FGT bits
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[05-06 17:43]** [PATCH v4 18/43] KVM: arm64: Handle trapping of FEAT_LS64* instructions
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[05-06 17:43]** [PATCH v4 19/43] KVM: arm64: Restrict ACCDATA_EL1 undef to FEAT_LS64_ACCDATA being disabled
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[05-06 17:43]** [PATCH v4 20/43] KVM: arm64: Don't treat HCRX_EL2 as a FGT register
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[05-06 17:43]** [PATCH v4 21/43] KVM: arm64: Plug FEAT_GCS handling
   - 发件人: Marc Zyngier <maz@kernel.org>
23. **[05-06 17:43]** [PATCH v4 22/43] KVM: arm64: Compute FGT masks from KVM's own FGT tables
   - 发件人: Marc Zyngier <maz@kernel.org>
24. **[05-06 17:43]** [PATCH v4 23/43] KVM: arm64: Add description of FGT bits leading to EC!=0x18
   - 发件人: Marc Zyngier <maz@kernel.org>
25. **[05-06 17:43]** [PATCH v4 24/43] KVM: arm64: Use computed masks as sanitisers for FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
26. **[05-06 17:43]** [PATCH v4 25/43] KVM: arm64: Unconditionally configure fine-grain traps
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[05-06 17:43]** [PATCH v4 26/43] KVM: arm64: Propagate FGT masks to the nVHE hypervisor
   - 发件人: Marc Zyngier <maz@kernel.org>
28. **[05-06 17:43]** [PATCH v4 27/43] KVM: arm64: Use computed FGT masks to setup FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
29. **[05-06 17:43]** [PATCH v4 28/43] KVM: arm64: Remove hand-crafted masks for FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
30. **[05-06 17:43]** [PATCH v4 29/43] KVM: arm64: Use KVM-specific HCRX_EL2 RES0 mask
   - 发件人: Marc Zyngier <maz@kernel.org>
31. **[05-06 17:43]** [PATCH v4 30/43] KVM: arm64: Handle PSB CSYNC traps
   - 发件人: Marc Zyngier <maz@kernel.org>
32. **[05-06 17:43]** [PATCH v4 31/43] KVM: arm64: Switch to table-driven FGU configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
33. **[05-06 17:43]** [PATCH v4 32/43] KVM: arm64: Validate FGT register descriptions against RES0 masks
   - 发件人: Marc Zyngier <maz@kernel.org>
34. **[05-06 17:43]** [PATCH v4 33/43] KVM: arm64: Use FGT feature maps to drive RES0 bits
   - 发件人: Marc Zyngier <maz@kernel.org>
35. **[05-06 17:43]** [PATCH v4 34/43] KVM: arm64: Allow kvm_has_feat() to take variable arguments
   - 发件人: Marc Zyngier <maz@kernel.org>
36. **[05-06 17:43]** [PATCH v4 35/43] KVM: arm64: Use HCRX_EL2 feature map to drive fixed-value bits
   - 发件人: Marc Zyngier <maz@kernel.org>
37. **[05-06 17:43]** [PATCH v4 36/43] KVM: arm64: Use HCR_EL2 feature map to drive fixed-value bits
   - 发件人: Marc Zyngier <maz@kernel.org>
38. **[05-06 17:43]** [PATCH v4 37/43] KVM: arm64: Add FEAT_FGT2 registers to the VNCR page
   - 发件人: Marc Zyngier <maz@kernel.org>
39. **[05-06 17:43]** [PATCH v4 38/43] KVM: arm64: Add sanitisation for FEAT_FGT2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
40. **[05-06 17:43]** [PATCH v4 39/43] KVM: arm64: Add trap routing for FEAT_FGT2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
41. **[05-06 17:43]** [PATCH v4 40/43] KVM: arm64: Add context-switch for FEAT_FGT2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
42. **[05-06 17:43]** [PATCH v4 41/43] KVM: arm64: Allow sysreg ranges for FGT descriptors
   - 发件人: Marc Zyngier <maz@kernel.org>
43. **[05-06 17:43]** [PATCH v4 42/43] KVM: arm64: Add FGT descriptors for FEAT_FGT2
   - 发件人: Marc Zyngier <maz@kernel.org>
44. **[05-06 17:43]** [PATCH v4 43/43] KVM: arm64: Handle TSB CSYNC traps
   - 发件人: Marc Zyngier <maz@kernel.org>
45. **[05-08 14:49]** Re: [PATCH v4 27/43] KVM: arm64: Use computed FGT masks to setup FGT
 registers
   - 发件人: Joey Gouly <joey.gouly@arm.com>
46. **[05-08 16:58]** Re: [PATCH v4 31/43] KVM: arm64: Switch to table-driven FGU
 configuration
   - 发件人: Joey Gouly <joey.gouly@arm.com>
47. **[05-10 10:56]** Re: [PATCH v4 31/43] KVM: arm64: Switch to table-driven FGU configuration
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [PATCH v4 00/24] Tracefs support for pKVM

**📧 邮件数**: 32 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  6 May 2025 17:47:56 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 的 Tracefs 支持的补丁系列（[PATCH v4 00/24]），主要内容包括引入远程事件和简单环形缓冲区的实现，以便在受保护模式下进行调试和性能分析。

1. **原始补丁/问题内容**：
   本补丁系列旨在为 pKVM 超级管理程序引入 Tracefs 支持，提供一种简便的调试和性能分析工具。补丁包括创建远程事件、环形缓冲区和 Tracefs 接口的实现。

2. **之前讨论要点**：
   之前的讨论集中在如何设计远程环形缓冲区，使其能够与 Tracefs 兼容，并允许超管在内核和用户空间之间共享数据。参与者讨论了环形缓冲区的实现细节，以及如何确保数据一致性和性能。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，Vincent Donnefort 提出了多个补丁，涵盖了环形缓冲区的实现、Tracefs 接口的创建、事件支持的添加等。Steven Rostedt 提出了对补丁的改进建议，包括增加注释、处理错误返回值等。最终，补丁系列的目标是增强 pKVM 的可调试性和可追踪性，确保在受保护模式下能够有效地记录和分析事件。

#### 📝 邮件列表

1. **[05-06 17:47]** [PATCH v4 00/24] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[05-06 17:47]** [PATCH v4 01/24] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[05-06 17:47]** [PATCH v4 02/24] tracing: Introduce trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[05-06 17:47]** [PATCH v4 03/24] tracing: Add reset to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[05-06 17:48]** [PATCH v4 04/24] tracing: Add init callback to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[05-06 17:48]** [PATCH v4 05/24] tracing: Add events to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[05-06 17:48]** [PATCH v4 06/24] tracing: Add events/ root files to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[05-06 17:48]** [PATCH v4 07/24] tracing: Add helpers to create trace remote events
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[05-06 17:48]** [PATCH v4 08/24] ring-buffer: Expose buffer_data_page material
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[05-06 17:48]** [PATCH v4 09/24] tracing: Introduce simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[05-06 17:48]** [PATCH v4 10/24] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[05-06 17:48]** [PATCH v4 11/24] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
13. **[05-06 17:48]** [PATCH v4 12/24] tracing: load/unload page callbacks for simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
14. **[05-06 17:48]** [PATCH v4 13/24] tracing: Check for undefined symbols in simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
15. **[05-06 17:48]** [PATCH v4 14/24] KVM: arm64: Support unaligned fixmap in the nVHE hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
16. **[05-06 17:48]** [PATCH v4 15/24] KVM: arm64: Add .hyp.data section
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
17. **[05-06 17:48]** [PATCH v4 16/24] KVM: arm64: Add clock support for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
18. **[05-06 17:48]** [PATCH v4 17/24] KVM: arm64: Add tracing capability for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
19. **[05-06 17:48]** [PATCH v4 18/24] KVM: arm64: Add trace remote for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
20. **[05-06 17:48]** [PATCH v4 19/24] KVM: arm64: Sync boot clock with the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
21. **[05-06 17:48]** [PATCH v4 20/24] KVM: arm64: Add trace reset to the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
22. **[05-06 17:48]** [PATCH v4 21/24] KVM: arm64: Add event support to the pKVM hyp and
 trace remote
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
23. **[05-06 17:48]** [PATCH v4 22/24] KVM: arm64: Add hyp_enter/hyp_exit events to pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
24. **[05-06 17:48]** [PATCH v4 23/24] KVM: arm64: Add selftest event support to pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
25. **[05-06 17:48]** [PATCH v4 24/24] tracing: selftests: Add pKVM trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
26. **[05-07 19:47]** Re: [PATCH v4 01/24] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
27. **[05-07 20:24]** Re: [PATCH v4 02/24] tracing: Introduce trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
28. **[05-08 10:10]** Re: [PATCH v4 01/24] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
29. **[05-08 10:14]** Re: [PATCH v4 02/24] tracing: Introduce trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
30. **[05-08 10:05]** Re: [PATCH v4 01/24] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
31. **[05-09 15:47]** Re: [PATCH v4 05/24] tracing: Add events to trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
32. **[05-09 15:54]** Re: [PATCH v4 08/24] ring-buffer: Expose buffer_data_page material
   - 发件人: Steven Rostedt <rostedt@goodmis.org>

---

### Thread 3: [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation

**📧 邮件数**: 19 | **👥 参与者**: 6 | **📅 开始时间**: Thu, 1 May 2025 20:52:39 -0700

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 FF-A（Firmware Framework for Arm）主机版本重新协商的限制。原始的补丁（PATCH 1/3）旨在防止主机在已经协商的版本基础上请求较低的 FF-A 版本，因为这可能导致不兼容的问题。

在历史讨论中，Per Larsen 提出了补丁的背景，指出 FF-A 1.1 版本在多个结构上破坏了 ABI（应用二进制接口），而 FF-A 1.2 则依赖于 SMCCC 1.2，且不向后兼容。Marc Zyngier 对补丁的格式和内容提出了批评，认为需要更清晰的表述，并质疑为何超管需要处理规范中的缺陷。

在本周的新讨论中，Per Larsen 表示将修正补丁的格式，并讨论了补丁的必要性。他指出，一旦协商了版本，主机不应再尝试重新协商。Sebastian Ene 提出简化补丁描述的建议，并讨论了如何处理 SMC（Secure Monitor Call）接口的锁定问题。Marc Zyngier 和 Sudeep Holla 进一步讨论了补丁的实现细节和潜在的兼容性问题，强调了在主机和超管之间保持版本一致性的重要性。

总体来看，本周的讨论集中在补丁的清晰性、实现细节和对 FF-A 版本协商的必要性上，参与者们对如何确保系统的稳定性和兼容性进行了深入探讨。

#### 📝 邮件列表

1. **[05-01 20:52]** [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: Per Larsen <perl@immunant.com>
2. **[05-02 09:47]** Re: [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[05-02 02:21]** [PATCH 0/3] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen <perl@immunant.com>
4. **[05-02 02:21]** [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: Per Larsen <perl@immunant.com>
5. **[05-02 02:21]** [PATCH 2/3] KVM: arm64: Bump the supported version of FF-A to 1.2
   - 发件人: Per Larsen <perl@immunant.com>
6. **[05-02 02:21]** [PATCH 3/3] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in host handler
   - 发件人: Per Larsen <perl@immunant.com>
7. **[05-06 02:29]** Re: [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: Per Larsen <perl@immunant.com>
8. **[05-06 10:10]** Re: [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: Sebastian Ene <sebastianene@google.com>
9. **[05-06 12:01]** Re: [PATCH 2/3] KVM: arm64: Bump the supported version of FF-A to 1.2
   - 发件人: Sebastian Ene <sebastianene@google.com>
10. **[05-06 12:16]** Re: [PATCH 3/3] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in host
 handler
   - 发件人: Sebastian Ene <sebastianene@google.com>
11. **[05-08 09:55]** Re: [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[05-08 10:26]** Re: [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
13. **[05-08 08:45]** Re: [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: =?UTF-8?B?QXJ2ZSBIasO4bm5ldsOlZw==?= <arve@android.com>
14. **[05-08 17:07]** Re: [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
15. **[05-09 16:33]** [PATCH 0/3] KVM: arm64: selftests: arch_timer_edge_cases fixes
   - 发件人: Sebastian Ott <sebott@redhat.com>
16. **[05-09 16:33]** [PATCH 1/3] KVM: arm64: selftests: fix help text for arch_timer_edge_cases
   - 发件人: Sebastian Ott <sebott@redhat.com>
17. **[05-09 16:33]** [PATCH 2/3] KVM: arm64: selftests: fix thread migration in arch_timer_edge_cases
   - 发件人: Sebastian Ott <sebott@redhat.com>
18. **[05-09 16:33]** [PATCH 3/3] KVM: arm64: selftests: arch_timer_edge_cases - workaround for AC03_CPU_14
   - 发件人: Sebastian Ott <sebott@redhat.com>
19. **[05-10 10:03]** Re: [PATCH 3/3] KVM: arm64: selftests: arch_timer_edge_cases - workaround for AC03_CPU_14
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 4: [PATCH 0/8] stackleak: Support Clang stack depth tracking

**📧 邮件数**: 15 | **👥 参与者**: 5 | **📅 开始时间**: Wed,  7 May 2025 11:16:06 -0700

#### 🤖 AI 总结

本邮件线程讨论的主题是关于支持 Clang 堆栈深度跟踪的 stackleak 特性，涉及到一系列补丁（PATCH 0/8 至 PATCH 8/8）。

1. **原始补丁/问题内容**：
   Kees Cook 提出了一个补丁系列，旨在利用 Clang 的堆栈深度跟踪回调来实现 stackleak 功能。这一特性可以在系统调用返回时清除内核堆栈，以减少潜在的堆栈泄漏风险。

2. **之前讨论要点**：
   在历史讨论中，Kees 提到希望将 GCC 插件替换为 Clang 实现，并且在补丁中对架构特定的 Makefile 进行了调整。此外，补丁中还涉及到对 CONFIG_GCC_PLUGIN_STACKLEAK 的重命名，以更好地反映其功能。

3. **本周的新讨论、进展或结论**：
   本周的讨论集中在补丁的具体实现上，包括：
   - 将 `stackleak_track_stack` 函数重命名为 `__sanitizer_cov_stack_depth`，以符合 Clang 的命名规范。
   - 将 stackleak 的 CFLAGS 从 GCC_PLUGINS_CFLAGS 中分离出来，创建了新的 STACKLEAK_CFLAGS。
   - 启用 CONFIG_STACKLEAK 以支持 Clang 和 GCC 插件的堆栈清除功能。
   - 参与者对补丁进行了审查，并提出了对命名的建议，认为应更清晰地反映其功能。

整体来看，本周的讨论推动了 stackleak 特性的实现，并加强了对内核安全性的关注。

#### 📝 邮件列表

1. **[05-07 11:16]** [PATCH 0/8] stackleak: Support Clang stack depth tracking
   - 发件人: Kees Cook <kees@kernel.org>
2. **[05-07 11:16]** [PATCH 1/8] nvme-pci: Make nvme_pci_npages_prp() __always_inline
   - 发件人: Kees Cook <kees@kernel.org>
3. **[05-07 11:16]** [PATCH 2/8] init.h: Disable sanitizer coverage for __init and __head
   - 发件人: Kees Cook <kees@kernel.org>
4. **[05-07 11:16]** [PATCH 3/8] stackleak: Rename CONFIG_GCC_PLUGIN_STACKLEAK to CONFIG_STACKLEAK
   - 发件人: Kees Cook <kees@kernel.org>
5. **[05-07 11:16]** [PATCH 4/8] stackleak: Rename stackleak_track_stack to __sanitizer_cov_stack_depth
   - 发件人: Kees Cook <kees@kernel.org>
6. **[05-07 11:16]** [PATCH 5/8] stackleak: Split STACKLEAK_CFLAGS from GCC_PLUGINS_CFLAGS
   - 发件人: Kees Cook <kees@kernel.org>
7. **[05-07 11:16]** [PATCH 6/8] stackleak: Support Clang stack depth tracking
   - 发件人: Kees Cook <kees@kernel.org>
8. **[05-07 11:16]** [PATCH 7/8] configs/hardening: Enable CONFIG_STACKLEAK
   - 发件人: Kees Cook <kees@kernel.org>
9. **[05-07 11:16]** [PATCH 8/8] configs/hardening: Enable CONFIG_INIT_ON_FREE_DEFAULT_ON
   - 发件人: Kees Cook <kees@kernel.org>
10. **[05-07 12:22]** Re: [PATCH 1/8] nvme-pci: Make nvme_pci_npages_prp() __always_inline
   - 发件人: Keith Busch <kbusch@kernel.org>
11. **[05-07 20:45]** Re: [PATCH 3/8] stackleak: Rename CONFIG_GCC_PLUGIN_STACKLEAK to
 CONFIG_STACKLEAK
   - 发件人: Ingo Molnar <mingo@kernel.org>
12. **[05-07 12:36]** Re: [PATCH 3/8] stackleak: Rename CONFIG_GCC_PLUGIN_STACKLEAK to
 CONFIG_STACKLEAK
   - 发件人: Kees Cook <kees@kernel.org>
13. **[05-07 21:39]** Re: [PATCH 3/8] stackleak: Rename CONFIG_GCC_PLUGIN_STACKLEAK to
 CONFIG_STACKLEAK
   - 发件人: Ingo Molnar <mingo@kernel.org>
14. **[05-08 14:22]** Re: [PATCH 2/8] init.h: Disable sanitizer coverage for __init and __head
   - 发件人: Marco Elver <elver@google.com>
15. **[05-08 14:25]** Re: [PATCH 2/8] init.h: Disable sanitizer coverage for __init and __head
   - 发件人: Dmitry Vyukov <dvyukov@google.com>

---

### Thread 5: [PATCH v6 00/14] arm: rework id register storage

**📧 邮件数**: 15 | **👥 参与者**: 1 | **📅 开始时间**: Tue,  6 May 2025 10:52:20 +0200

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 ARM 架构的 ID 寄存器存储重构的补丁系列（[PATCH v6 00/14] arm: rework id register storage）。该补丁系列旨在改进 ARM CPU 模型中 ID 寄存器的存储和访问方式。

1. **原始补丁/问题的内容**：
   - 该补丁系列的目标是重新设计 ARM 架构中 ID 寄存器的存储方式，具体包括将 ID 寄存器从结构体中的命名字段迁移到数组中，以便更高效地管理和访问。

2. **之前的讨论要点**：
   - 之前的讨论中提到，补丁系列经历了多个版本的迭代，主要改进包括合并补丁、修复转换错误、添加缺失的 SPDX 头文件等。参与者对补丁的结构和实现细节进行了多次审查和反馈。

3. **本周的新讨论、进展或结论**：
   - 本周的讨论中，Cornelia Huck 提出了对补丁的进一步修改，包括修复了一些转换错误，并重新基于当前的主干代码进行了补丁的更新。此外，Eric Auger 提出了新的补丁，增加了对 ID 寄存器的定义和生成脚本，以便从 Linux 源树中自动生成系统寄存器定义。最终，补丁得到了审查并被接受，标志着这一系列补丁的进展和完善。

#### 📝 邮件列表

1. **[05-06 10:52]** [PATCH v6 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[05-06 10:52]** [PATCH v6 01/14] arm/cpu: Add sysreg definitions in cpu-sysregs.h
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[05-06 10:52]** [PATCH v6 02/14] arm/cpu: Store aa64isar0/aa64zfr0 into the idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>
4. **[05-06 10:52]** [PATCH v6 03/14] arm/cpu: Store aa64isar1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
5. **[05-06 10:52]** [PATCH v6 04/14] arm/cpu: Store aa64pfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
6. **[05-06 10:52]** [PATCH v6 05/14] arm/cpu: Store aa64mmfr0-3 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
7. **[05-06 10:52]** [PATCH v6 06/14] arm/cpu: Store aa64dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
8. **[05-06 10:52]** [PATCH v6 07/14] arm/cpu: Store aa64smfr0 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
9. **[05-06 10:52]** [PATCH v6 08/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
10. **[05-06 10:52]** [PATCH v6 09/14] arm/cpu: Store id_pfr0/1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
11. **[05-06 10:52]** [PATCH v6 10/14] arm/cpu: Store id_dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
12. **[05-06 10:52]** [PATCH v6 11/14] arm/cpu: Store id_mmfr0-5 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
13. **[05-06 10:52]** [PATCH v6 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
14. **[05-06 10:52]** [PATCH v6 13/14] arm/cpu: switch to a generated cpu-sysregs.h.inc
   - 发件人: Cornelia Huck <cohuck@redhat.com>
15. **[05-06 10:52]** [PATCH v6 14/14] arm/kvm: use fd instead of fdarray[2]
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 6: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags

**📧 邮件数**: 13 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 23 Apr 2025 11:45:04 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（内核虚拟机）在 arm64 架构下的补丁，主题为“允许使用 VMA（虚拟内存区域）标志进行可缓存的二级映射”。该补丁旨在改善 KVM 对可缓存内存的支持。

在历史讨论中，参与者们探讨了补丁的必要性及其实现方式，提出了使用基于文件描述符（fd）的方式来处理可缓存映射的可能性，并讨论了如何在没有 VMA 的情况下传达映射属性。Jason Gunthorpe 强调了确保 KVM 不会创建非缓存映射的必要性，并提到缺乏缓存维护是 vfio-grace 设备的主要问题。

在本周的新讨论中，Ankit Agrawal 提出希望添加对 ARM64_HAS_CACHE_DIC 的检查，以确保补丁的安全性，特别是在可执行映射的情况下。同时，他也询问其他参与者是否应该添加 memslot 标志，以便更好地管理可缓存 PFNMAP（页框号映射）。Catalin Marinas 表示只要不遗漏某些硬件支持 FWB（写回缓存）但不支持 DIC（数据缓存无效化），他对此表示赞同。

总体来看，讨论集中在补丁的实现细节及其对不同硬件支持的影响上，参与者们对补丁的方向表示认可，但仍需进一步明确实现细节。

#### 📝 邮件列表

1. **[04-23 11:45]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
2. **[04-23 09:02]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
3. **[04-23 13:26]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[04-23 10:03]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
5. **[04-29 10:47]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
6. **[04-29 14:27]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
7. **[04-29 11:14]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
8. **[04-29 17:03]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
9. **[04-29 13:44]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
10. **[04-29 19:09]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
11. **[04-29 15:19]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
12. **[05-07 15:26]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
13. **[05-09 13:47]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 7: [PATCH v4 00/10] Stage-2 huge mappings for pKVM np-guests

**📧 邮件数**: 11 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  9 May 2025 14:16:56 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 非特权虚拟机（np-guests）支持的阶段二大页映射（Stage-2 huge mappings）的补丁系列（PATCH v4 00/10）。该系列补丁的主要目标是为 pKVM np-guests 添加 PMD_SIZE 级别的映射，以便在 Stage-1 由 Hugetlbfs 或 THPs 支持时安装 PMD 级别的映射。

在历史讨论中，补丁的演变过程包括多个版本的修改，主要集中在修复 PUD_SIZE 到 PMD_SIZE 的强制执行、优化共享映射的实现以及减少页表遍历的次数等方面。此外，补丁还引入了新的辅助函数，以便于处理大页映射。

本周的新讨论中，参与者 Vincent Donnefort 提交了十个补丁，涵盖了以下关键内容：
1. 增加了对 np-guest CMO 的处理，使其支持 PMD_SIZE 的映射。
2. 引入了一个迭代超管虚拟内存映射的辅助函数。
3. 修改了多个超调用（hypercall），以支持 nr_pages 参数，允许在共享和取消共享时指定映射的页数。
4. 引入了一个共享的 PMD_SIZE fixmap，以提高在安装阶段二大页映射时的性能。

最后，补丁系列的最后一个补丁实现了 np-guests 的阶段二大页映射，显著提升了在处理大页时的性能，尤其是在减少延迟方面。整体来看，这一系列补丁为 pKVM 的大页支持奠定了基础，提升了虚拟化性能。

#### 📝 邮件列表

1. **[05-09 14:16]** [PATCH v4 00/10] Stage-2 huge mappings for pKVM np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[05-09 14:16]** [PATCH v4 01/10] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[05-09 14:16]** [PATCH v4 02/10] KVM: arm64: Introduce for_each_hyp_page
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[05-09 14:16]** [PATCH v4 03/10] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[05-09 14:17]** [PATCH v4 04/10] KVM: arm64: Add a range to __pkvm_host_unshare_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[05-09 14:17]** [PATCH v4 05/10] KVM: arm64: Add a range to __pkvm_host_wrprotect_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[05-09 14:17]** [PATCH v4 06/10] KVM: arm64: Add a range to __pkvm_host_test_clear_young_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[05-09 14:17]** [PATCH v4 07/10] KVM: arm64: Convert pkvm_mappings to interval tree
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[05-09 14:17]** [PATCH v4 08/10] KVM: arm64: Add a range to pkvm_mappings
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[05-09 14:17]** [PATCH v4 09/10] KVM: arm64: Stage-2 huge mappings for np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[05-09 14:17]** [PATCH v4 10/10] KVM: arm64: np-guest CMOs with PMD_SIZE fixmap
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 8: [PATCH 00/10] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 11 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 06 May 2025 12:41:32 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARMv8.8 SPE（可扩展性能监控）特性的补丁集，共包含10个补丁，主要集中在支持新特性和相关工具的更新。

1. **原始补丁内容**：补丁集旨在支持三个新特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 SPE_FEAT_FDS 数据源过滤。这些特性是独立的，可以分别应用。

2. **之前讨论要点**：虽然没有具体的历史讨论记录，但可以推测这些补丁是基于对 ARM 架构性能监控功能的持续改进和扩展需求，尤其是在数据源过滤和扩展过滤方面。

3. **本周新讨论及进展**：本周的讨论集中在补丁的具体实现上，包括：
   - 增加了新的系统寄存器字段以支持新特性（补丁1）。
   - 实现了 FEAT_SPEv1p4 和 FEAT_SPE_EFT 的支持（补丁2和3）。
   - 详细描述了 SPE_FEAT_FDS 的实现，包括数据源过滤的功能（补丁4-8）。
   - 引入了新的 `config4` 字段以支持新的过滤控制（补丁6）。
   - 更新了文档以反映新特性的使用方法（补丁10）。

整体来看，这一系列补丁旨在增强 ARM 架构的性能监控能力，提供更灵活的过滤选项，以满足日益增长的性能分析需求。

#### 📝 邮件列表

1. **[05-06 12:41]** [PATCH 00/10] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[05-06 12:41]** [PATCH 01/10] arm64: sysreg: Add new PMSIDR_EL1 and PMSFCR_EL1
 fields
   - 发件人: James Clark <james.clark@linaro.org>
3. **[05-06 12:41]** [PATCH 02/10] perf: arm_spe: Support FEAT_SPEv1p4 filters
   - 发件人: James Clark <james.clark@linaro.org>
4. **[05-06 12:41]** [PATCH 03/10] perf: arm_spe: Add support for FEAT_SPE_EFT extended
 filtering
   - 发件人: James Clark <james.clark@linaro.org>
5. **[05-06 12:41]** [PATCH 04/10] arm64/boot: Enable EL2 requirements for SPE_FEAT_FDS
   - 发件人: James Clark <james.clark@linaro.org>
6. **[05-06 12:41]** [PATCH 05/10] KVM: arm64: Add trap configs for PMSDSFR_EL1
   - 发件人: James Clark <james.clark@linaro.org>
7. **[05-06 12:41]** [PATCH 06/10] perf: Add perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
8. **[05-06 12:41]** [PATCH 07/10] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: James Clark <james.clark@linaro.org>
9. **[05-06 12:41]** [PATCH 08/10] tools headers UAPI: Sync linux/perf_event.h with the
 kernel sources
   - 发件人: James Clark <james.clark@linaro.org>
10. **[05-06 12:41]** [PATCH 09/10] perf tools: Add support for perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
11. **[05-06 12:41]** [PATCH 10/10] perf docs: arm-spe: Document new SPE filtering
 features
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 9: [PATCH 0/2] KVM: arm64: Make AArch64 support sticky

**📧 邮件数**: 10 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 29 Apr 2025 12:41:15 +0100

#### 🤖 AI 总结

本邮件线程讨论了与 KVM（Kernel-based Virtual Machine）相关的两个补丁，主要针对 arm64 架构的 AArch64 支持和自测试功能的改进。

1. **原始补丁内容**：Marc Zyngier 提出的补丁旨在使 AArch64 支持在 KVM 中保持“粘性”，即防止用户空间在任何可虚拟化的执行级别禁用 AArch64 支持。此外，补丁还修复了测试套件中写入零值到 ID_AA64PFR0_EL1 的问题。

2. **之前讨论要点**：历史讨论中提到，当前的测试套件存在问题，导致 KVM 在运行时可能会错误地禁用 AArch64 支持，进而引发未定义的行为。Marc Zyngier 还指出，HCRX_EL2 的处理在主机上存在缺陷，需进行修复。

3. **本周的新讨论与进展**：本周的讨论主要集中在自测试功能的改进上。参与者 Vipin Sharma 和 Sean Christopherson 讨论了如何自动生成默认测试用例，以及如何改进测试运行器的命令行选项和输出格式。Oliver Upton 确认已将 Marc Zyngier 的补丁应用到修复中，确保 AArch64 支持的稳定性和测试功能的增强。

总体而言，本周的讨论推动了 KVM 的自测试功能向更高效和灵活的方向发展，同时确保了 AArch64 支持的可靠性。

#### 📝 邮件列表

1. **[04-29 12:41]** [PATCH 0/2] KVM: arm64: Make AArch64 support sticky
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[04-30 11:59]** [PATCH 0/2] KVM: arm64: Fix HCRX_EL2.GCSEn handling
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[04-30 10:01]** Re: [PATCH 1/2] KVM: selftests: Add default testfiles for KVM
 selftests runner
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[04-30 14:31]** Re: [PATCH 2/2] KVM: selftests: Create KVM selftest runner
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[05-05 12:05]** Re: [PATCH 1/2] KVM: selftests: Add default testfiles for KVM
 selftests runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
6. **[05-05 12:48]** Re: [PATCH 2/2] KVM: selftests: Create KVM selftest runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
7. **[05-05 15:57]** Re: [PATCH 1/2] KVM: selftests: Add default testfiles for KVM
 selftests runner
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[05-05 16:26]** Re: [PATCH 2/2] KVM: selftests: Create KVM selftest runner
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[05-07 00:56]** Re: [PATCH 0/2] KVM: arm64: Fix HCRX_EL2.GCSEn handling
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[05-07 00:56]** Re: [PATCH 0/2] KVM: arm64: Make AArch64 support sticky
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 10: [PATCH v1 0/6] VMM can handle guest SEA via KVM_EXIT_ARM_SEA

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  5 May 2025 16:14:06 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 中处理客体的同步外部中止（SEA）的补丁集。补丁集的核心内容是通过 KVM_EXIT_ARM_SEA 机制，让虚拟机监控器（VMM）能够更优雅地处理内存错误，避免直接注入异步 SError 导致客体内核崩溃。

**历史讨论：**
该补丁集的背景是，当主机的 APEI 无法处理阶段 2 的 SEA 时，KVM 目前的做法是直接向虚拟 CPU 注入异步 SError，通常会导致客体内核崩溃。讨论中提到，客体 SEA 常见于虚拟 CPU 消耗可恢复的未更正内存错误（UER），而直接注入 SError 虽能阻止错误传播，但缺乏优雅的恢复方式。

**本周新讨论：**
本周的讨论集中在补丁集的具体实现上，包括以下几个关键点：
1. **新功能引入**：补丁集引入了 KVM_CAP_ARM_SEA_TO_USER 和 KVM_EXIT_ARM_SEA 等新用户空间可见的功能，使得用户空间能够在处理 SEA 时接收更多信息。
2. **用户空间的参与**：用户空间可以选择处理 SEA，KVM 将在发生 SEA 时退出到用户空间，提供详细的错误信息，用户空间可以根据这些信息决定如何处理错误。
3. **测试用例**：补丁集还包括自测试，验证 KVM 在处理 SEA 时的行为是否符合预期，确保用户空间能够正确处理 SEA 事件。

总之，本周的讨论展示了补丁集的进展，强调了用户空间在处理内存错误中的重要性，以及如何通过新引入的 API 改善 KVM 的错误处理能力。

#### 📝 邮件列表

1. **[05-05 16:14]** [PATCH v1 0/6] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[05-05 16:14]** [PATCH v1 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[05-05 16:14]** [PATCH v1 2/6] KVM: arm64: Set FnV for VCPU when FAR_EL2 is invalid
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
4. **[05-05 16:14]** [PATCH v1 3/6] KVM: arm64: Allow userspace to inject external
 instruction aborts
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
5. **[05-05 16:14]** [PATCH v1 4/6] KVM: selftests: Test for KVM_EXIT_ARM_SEA and KVM_CAP_ARM_SEA_TO_USER
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
6. **[05-05 16:14]** [PATCH v1 5/6] KVM: selftests: Test for KVM_CAP_INJECT_EXT_IABT
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
7. **[05-05 16:14]** [PATCH v1 6/6] Documentation: kvm: new uAPI for handling SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
8. **[05-08 00:54]** Re: [PATCH v1 6/6] Documentation: kvm: new uAPI for handling SEA
   - 发件人: ALOK TIWARI <alok.a.tiwari@oracle.com>

---

### Thread 11: [PATCH v2 0/4] KVM: arm64: UBSAN at EL2

**📧 邮件数**: 6 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 30 Apr 2025 16:27:07 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 的 arm64 架构中支持 UBSAN（Undefined Behavior Sanitizer）功能的补丁集。历史讨论中，Mostafa Saleh 提出了这一补丁集，旨在解决在 EL2 模式下，许多内核支持的 sanitizers 被禁用的问题。补丁集包含四个部分，主要是为 EL2 引入 UBSAN 支持，增加了相应的配置和处理逻辑。

在之前的讨论中，Kees Cook 表达了对补丁集的支持，并提到希望通过适当的树合并该补丁，以避免未来的冲突。

本周的新讨论中，Marc Zyngier 更新了补丁的进展，确认已将补丁应用到下一版本中，并提供了稳定分支以供其他人拉取和解决潜在冲突。Kees Cook 也确认了补丁已被纳入 kvmarm/next，并表示稳定分支已可用。整体来看，补丁集的合并进展顺利，参与者之间的沟通良好。

#### 📝 邮件列表

1. **[04-30 16:27]** [PATCH v2 0/4] KVM: arm64: UBSAN at EL2
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[04-30 11:32]** Re: [PATCH v2 0/4] KVM: arm64: UBSAN at EL2
   - 发件人: Kees Cook <kees@kernel.org>
3. **[05-06 09:36]** Re: [PATCH v2 0/4] KVM: arm64: UBSAN at EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[05-07 11:35]** Re: [PATCH v2 0/4] KVM: arm64: UBSAN at EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[05-07 11:35]** Re: [PATCH v2 0/4] KVM: arm64: UBSAN at EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[05-08 09:29]** Re: [PATCH v2 0/4] KVM: arm64: UBSAN at EL2
   - 发件人: Kees Cook <kees@kernel.org>

---

### Thread 12: [PATCH v2 00/13] KVM: Introduce KVM Userfault

**📧 邮件数**: 6 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 6 May 2025 16:48:00 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）引入用户故障（Userfault）的补丁系列，共包含 13 个补丁。补丁的主要目的是为 KVM 添加用户故障支持，以提高虚拟机内存管理的灵活性和效率。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出该补丁系列的背景是为了改善 KVM 的内存管理功能，特别是在处理用户空间的页面故障时。参与者们之前讨论了补丁的设计目标和实现细节，强调了不同架构间的依赖关系。

在本周的新讨论中，主要参与者 Sean Christopherson 和 James Houghton 对补丁进行了深入的审查和反馈。Houghton 提出补丁的粒度过细，建议将多个小补丁合并为一个，以简化代码和减少架构间的依赖。此外，他还建议在补丁中增加设计目标的详细说明，并提出了一些代码实现的优化建议，包括引入通用的 `struct kvm_page_fault` 结构体以提高可读性和维护性。

总体来看，本周的讨论集中在补丁的合并、代码优化及设计目标的明确化上，参与者们对该补丁系列的前景持积极态度，并认为这是支持后复制（post-copy）guest_memfd 的最佳提案。

#### 📝 邮件列表

1. **[05-06 16:48]** Re: [PATCH v2 00/13] KVM: Introduce KVM Userfault
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[05-06 17:01]** Re: [PATCH v2 01/13] KVM: Add KVM_MEM_USERFAULT memslot flag and bitmap
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[05-06 17:03]** Re: [PATCH v2 03/13] KVM: Allow late setting of KVM_MEM_USERFAULT on
 guest_memfd memslot
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[05-06 17:05]** Re: [PATCH v2 05/13] KVM: x86/mmu: Add support for KVM_MEM_USERFAULT
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[05-06 17:06]** Re: [PATCH v2 06/13] KVM: arm64: Add support for KVM_MEM_USERFAULT
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[05-06 17:13]** Re: [PATCH v2 00/13] KVM: Introduce KVM Userfault
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 13: [PATCH v3 00/17] KVM: arm64: Recursive NV support

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 23 Apr 2025 16:14:51 +0100

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（内核虚拟机）在 ARM64 架构下实现递归 NV（Nested Virtualization）支持的补丁（PATCH v3 00/17）。该补丁的核心是通过 FEAT_NV2 特性，使得虚拟机能够在访问系统寄存器时，诱导其访问内存，从而实现高效的上下文切换。补丁中提到的 VNCR 页面将用于处理这些寄存器访问。

在历史讨论中，Marc Zyngier 提出了补丁的基本思路，并具体描述了如何在 ARMv8.4-NV 支持的系统上分配 VNCR 页面，以满足系统寄存器的访问需求。该补丁得到了 Ganapatrao Kulkarni 的审核和支持。

在本周的新讨论中，Oliver Upton 提出补丁中可能需要使用 GFP_KERNEL_ACCOUNT 进行内存分配，这一建议得到了 Marc Zyngier 的认可，并表示将会将其整合到补丁中。整体来看，本周的讨论主要集中在补丁的细节优化上，推动了该功能的进一步完善。

#### 📝 邮件列表

1. **[04-23 16:14]** [PATCH v3 00/17] KVM: arm64: Recursive NV support
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[04-23 16:14]** [PATCH v3 02/17] KVM: arm64: nv: Allocate VNCR page when required
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[05-09 03:11]** Re: [PATCH v3 02/17] KVM: arm64: nv: Allocate VNCR page when required
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[05-09 16:57]** Re: [PATCH v3 02/17] KVM: arm64: nv: Allocate VNCR page when required
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [PATCH V2] arm64/mm: Implement pte_po_index() for permission
 overlay index

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 29 Apr 2025 16:11:36 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 arm64 架构下实现 `pte_po_index()` 函数，以支持权限覆盖索引的补丁（PATCH V2）。该补丁的背景是 Anshuman Khandual 正在开发一个支持 D128 页表的私有分支，但尚未准备好将其合并到主线中。

在历史讨论中，Will Deacon 和 Ryan Roberts 提到，Anshuman 的补丁旨在解决 D128 页表支持的相关问题，尽管目前仍存在许多未解答的问题。Ryan 强调，当前的补丁主要是一些无害的清理和重组，不会影响现有的 64 位页表管理。

在本周的新讨论中，Anshuman 认可了之前的观点，指出这些补丁有助于为 D128 的启用做准备，并强调了将 KVM 相关的更改与此补丁分开的必要性。然而，Will 对此表示反对，认为移除使用辅助宏的做法可能会导致代码的混乱，建议应让 `FIELD_GET()` 函数支持 128 位类型，以保持代码的一致性和清晰性。

总体来看，本周的讨论集中在补丁的设计选择及其对未来 D128 页表支持的影响上，参与者对如何处理代码的清理和重组存在不同看法。

#### 📝 邮件列表

1. **[04-29 16:11]** Re: [PATCH V2] arm64/mm: Implement pte_po_index() for permission
 overlay index
   - 发件人: Will Deacon <will@kernel.org>
2. **[04-29 17:45]** Re: [PATCH V2] arm64/mm: Implement pte_po_index() for permission
 overlay index
   - 发件人: Ryan Roberts <ryan.roberts@arm.com>
3. **[05-05 14:20]** Re: [PATCH V2] arm64/mm: Implement pte_po_index() for permission
 overlay index
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[05-09 16:02]** Re: [PATCH V2] arm64/mm: Implement pte_po_index() for permission
 overlay index
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 15: [PATCH v2 0/3] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 08 May 2025 08:38:51 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 FF-A 1.2 及 SEND_DIRECT2 ABI 的支持，涉及三个补丁（patch）。

1. **原始补丁内容**：补丁集的主要目的是实现对 FF-A 1.2 版本的支持，特别是新的 SEND_DIRECT2 ABI。该 ABI 允许使用寄存器 x4-x17 来传递消息负载。补丁确保主机不会使用低于与虚拟机监控器（hypervisor）协商的 FF-A 版本，以避免兼容性问题。

2. **之前的讨论要点**：虽然本邮件没有提供历史讨论的详细信息，但可以推测，之前的讨论可能集中在 FF-A 版本的兼容性和如何有效地实现新接口的支持上。

3. **本周的新讨论与进展**：本周的讨论主要围绕三个补丁的具体实现。第一个补丁限制主机与虚拟机监控器重新协商较低版本的 FF-A；第二个补丁将支持的 FF-A 版本提升至 1.2，并更新相关函数以支持新的 SMC 调用约定；第三个补丁则在主机处理程序中添加对 FFA_MSG_SEND_DIRECT_REQ2 的支持。所有补丁均经过测试，确保在 QEMU 环境下的 Android 启动过程中能够成功使用 SEND_DIRECT2 ABI。

总的来说，本周的讨论集中在实现 FF-A 1.2 的具体补丁和确保其在虚拟化环境中的有效性上，标志着对新标准的逐步适配。

#### 📝 邮件列表

1. **[05-08 08:38]** [PATCH v2 0/3] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[05-08 08:38]** [PATCH v2 1/3] KVM: arm64: Restrict FF-A host version
 renegotiation
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[05-08 08:38]** [PATCH v2 2/3] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[05-08 08:38]** [PATCH v2 3/3] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>

---

### Thread 16: [PATCH] KVM: arm64: Fix memory check in host_stage2_set_owner_locked()

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Thu,  1 May 2025 16:24:50 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 `host_stage2_set_owner_locked()` 函数中的内存检查问题。最初的补丁由 Mostafa Saleh 提出，指出在为 pKVM 准备补丁时发现了一个简单的错误，可能导致内核崩溃，尽管在正常情况下该错误似乎无害。

在历史讨论中，Mostafa 提到此补丁修复了一个与内存地址和大小相关的假设，认为 `addr_is_memory()` 函数在处理时是正确的。Marc Zyngier 对此提出了疑问，询问该假设是否发生了变化。

在本周的新讨论中，Mostafa 进一步解释了可能导致内存大小超出页面大小的情况，包括创建虚拟机时的结构体大小和 PGD（Page Global Directory）大小问题。最后，Oliver Upton 确认已将该补丁应用于修复列表，并感谢 Mostafa 的贡献。

总结来说，此次讨论围绕修复 KVM 中的内存检查问题展开，经过几轮讨论，补丁已被确认并应用。

#### 📝 邮件列表

1. **[05-01 16:24]** [PATCH] KVM: arm64: Fix memory check in host_stage2_set_owner_locked()
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[05-06 09:32]** Re: [PATCH] KVM: arm64: Fix memory check in host_stage2_set_owner_locked()
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[05-06 09:22]** Re: [PATCH] KVM: arm64: Fix memory check in
 host_stage2_set_owner_locked()
   - 发件人: Mostafa Saleh <smostafa@google.com>
4. **[05-07 00:56]** Re: [PATCH] KVM: arm64: Fix memory check in host_stage2_set_owner_locked()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 17: [PATCH v3 1/4] arm64: KVM: use mutex_trylock_nest_lock when locking all vCPUs

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 30 Apr 2025 16:23:08 -0400

#### 🤖 AI 总结

本邮件讨论的主题是关于在 arm64 KVM 中使用 `mutex_trylock_nest_lock` 来锁定所有虚拟 CPU (vCPUs) 的补丁。该补丁旨在解决当虚拟机配置的 vCPUs 超过 `MAX_LOCK_DEPTH` 时，触发的锁定正确性验证警告。

在历史讨论中，Maxim Levitsky 提出了这个补丁，指出使用 `mutex_trylock` 会导致锁定深度过高的错误警告，影响系统的稳定性。补丁的核心是替换锁定方法，以避免这些错误。

在本周的新讨论中，Marc Zyngier 提到该补丁已被应用到 `kvm-arm64/pkvm-selftest-6.16` 分支，并列出了相关的提交记录，显示补丁的进展情况。同时，内核测试机器人报告了在构建过程中出现的错误，指出补丁在某些构建环境下无法应用，并提供了详细的错误信息和建议。这表明该补丁在不同的代码树中可能存在兼容性问题，需要进一步的修复和调整。

#### 📝 邮件列表

1. **[04-30 16:23]** [PATCH v3 1/4] arm64: KVM: use mutex_trylock_nest_lock when locking all vCPUs
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
2. **[05-06 10:07]** Re: [PATCH v3 0/4] Selftest for pKVM ownership transitions
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[05-08 01:04]** Re: [PATCH v3 1/4] arm64: KVM: use mutex_trylock_nest_lock when
 locking all vCPUs
   - 发件人: kernel test robot <lkp@intel.com>

---

### Thread 18: [PATCH v8 15/43] arm64: RME: Allow VMM to set RIPAS

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 6 May 2025 14:23:24 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构下的 RME（Realm Management Extensions）功能，特别是允许虚拟机监控器（VMM）设置 RIPAS（Realm Identifier Page Address Space）。当前的讨论围绕着一个补丁（PATCH v8 15/43），该补丁旨在改进 VMM 对 RIPAS 的管理。

在历史讨论中，补丁的具体内容未被详细描述，但可以推测其目的是增强 ARM64 的虚拟化能力，确保在管理地址空间时的准确性和安全性。

本周的新讨论主要由参与者 Suzuki K Poulose 提出，针对补丁中的一些细节进行了多项建议和质疑。Suzuki 提到，可能需要在使用 RIPAS 的地方进行延迟处理，以避免错误的会计记录。此外，他还提出了对代码一致性和安全性的关注，例如建议对地址进行对齐处理，并讨论了在多线程环境下可能出现的竞争条件。他还提到，可能需要添加额外的调试信息，以便在出现问题时进行追踪。

总体而言，本周的讨论集中在补丁的细节改进和潜在的安全性问题上，参与者们对补丁的实现提出了建设性的反馈，旨在确保功能的正确性和稳定性。

#### 📝 邮件列表

1. **[05-06 14:23]** Re: [PATCH v8 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
2. **[05-07 11:26]** Re: [PATCH v8 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
3. **[05-07 11:42]** Re: [PATCH v8 17/43] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 19: [PATCH] KVM: arm64: Fix uninitialized memcache pointer in user_mem_abort()

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Mon,  5 May 2025 19:31:48 +0200

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 `user_mem_abort()` 函数中未初始化的内存缓存指针问题。

**原始补丁内容**：补丁由 Sebastian Ott 提出，修复了在 commit fce886a60207 中引入的一个问题，该提交使得 `user_mem_abort()` 函数中的本地内存缓存变量初始化变为条件性，从而在某些情况下可能使用未初始化的指针。这种情况可能导致在需要进行阶段二分配时出现故障。补丁确保内存缓存指针始终有效，以避免潜在的错误。

**之前讨论要点**：在历史讨论中并没有具体的内容记录，但可以推测该问题的引入与之前的代码变更有关，且补丁是对该变更的修复。

**本周的新讨论与进展**：本周的讨论主要集中在补丁的审查和应用上。Vincent Donnefort 对补丁进行了审核并表示认可，随后 Oliver Upton 确认已将补丁应用于修复分支。这表明补丁得到了积极的反馈并成功整合进代码库中。

#### 📝 邮件列表

1. **[05-05 19:31]** [PATCH] KVM: arm64: Fix uninitialized memcache pointer in user_mem_abort()
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[05-06 11:36]** Re: [PATCH] KVM: arm64: Fix uninitialized memcache pointer in
 user_mem_abort()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[05-07 00:56]** Re: [PATCH] KVM: arm64: Fix uninitialized memcache pointer in user_mem_abort()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 20: [PATCH v2] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE mode

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 29 Apr 2025 12:43:26 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在强制在 VHE（Virtual Host Extensions）模式下始终将 HCR_EL2.xMO 设置为 1。

**原始 patch/问题的内容**：Marc Zyngier 提出的补丁指出，当前在 VHE 模式下，动态设置和清除 HCR_EL2.xMO 位是没有必要的，因为我们始终希望物理中断能够到达主机，并且清除这些位会导致 IRQ（中断请求）无法被处理。此外，这种做法还会在 AmpereOne 硬件上触发一个严重的错误。

**之前的讨论要点**：在历史讨论中，Marc 阐述了补丁的必要性，强调了清除 HCR_EL2.xMO 位的潜在问题，包括中断处理的障碍和硬件错误。

**本周的新讨论、进展或结论**：在本周的讨论中，Marc Zyngier 和 Oliver Upton 确认该补丁已被应用到 kvm-arm64 的修复分支中，分别在邮件中表示感谢并确认了补丁的提交。这表明该补丁已经获得认可并成功整合到代码库中。

#### 📝 邮件列表

1. **[04-29 12:43]** [PATCH v2] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE mode
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[05-06 09:42]** Re: [PATCH v2] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE mode
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[05-07 00:56]** Re: [PATCH v2] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE mode
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 21: [PATCH v3] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  8 May 2025 14:00:09 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 AmpereOne 处理器的 erratum AC04_CPU_23 的修复补丁（PATCH v3）。该补丁旨在解决在 AC04 处理器上，HCR_EL2 的更新可能导致数据地址的同时翻译被破坏的问题。具体来说，只有由加载/存储指令发起的翻译会受到影响，而预取指令的翻译则不受影响。补丁中提出在对 HCR_EL2 进行存储之前插入 DSB 指令，并在之后插入 ISB 指令，以防止指令冲突导致的错误。

在之前的讨论中，补丁经历了多个版本的修改，主要集中在如何更有效地应用该工作区以及在汇编文件中捕获对 HCR_EL2 的存储操作。参与者们提出了不同的建议以优化补丁的实现。

在本周的新讨论中，D Scott Phillips 提交了补丁的最新版本，并得到了 Oliver Upton 的审查认可。Oliver 指出补丁仍需在文档中添加相关条目，以便记录该 erratum 的处理情况。整体而言，补丁的方向得到了认可，后续将继续完善文档部分。

#### 📝 邮件列表

1. **[05-08 14:00]** [PATCH v3] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
2. **[05-09 03:08]** Re: [PATCH v3] arm64: errata: Work around AmpereOne's erratum
 AC04_CPU_23
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 22: [PATCH] KVM: arm64: Drop sort_memblock_regions()

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 8 May 2025 18:59:50 +1000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，内容为“删除 sort_memblock_regions()”函数。该补丁旨在简化内存块区域的排序过程，提升系统性能。

在历史讨论中，虽然没有详细记录，但可以推测该补丁的提出是基于对现有内存管理机制的优化需求。参与者 Gavin Shan 提出了补丁，并询问是否需要在重新基线后重新发送补丁或进行其他操作，以便将其合并。

在本周的新讨论中，Gavin Shan 再次确认补丁的状态，并询问是否需要进一步的操作。Marc Zyngier 回复表示已经将该补丁应用到下一个版本中，并感谢 Gavin 的贡献。这表明补丁得到了认可并将进入后续的开发流程。

总结来说，本周的讨论主要集中在补丁的合并状态上，补丁“删除 sort_memblock_regions()”已成功应用，标志着该优化工作向前推进了一步。

#### 📝 邮件列表

1. **[05-08 18:59]** Re: [PATCH] KVM: arm64: Drop sort_memblock_regions()
   - 发件人: Gavin Shan <gshan@redhat.com>
2. **[05-08 11:32]** Re: [PATCH] KVM: arm64: Drop sort_memblock_regions()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 23: [PATCH v21 0/4] arm64/perf: Enable branch stack sampling

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 6 May 2025 15:47:02 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的性能监测补丁（PATCH v21 0/4），其目的是启用分支栈采样功能。该补丁的具体内容和实现细节在历史讨论中未详细列出，但可以推测它与性能监测和调试相关。

在之前的讨论中，参与者们关注补丁的审查进度和整合到现有代码中的问题。Jonathan Cameron 表达了希望尽快将重构版本整合到 OpenEuler 中的愿望，以避免频繁的代码更新。

在本周的新讨论中，Jonathan Cameron 询问了 Rob Herring 是否有关于补丁的更新或需要的帮助。Rob Herring 回复表示仍在等待 Mark R 的审查，并提到由于性能驱动程序的审查通常周期性进行，可能需要等待下一个周期才能得到反馈。这表明补丁的审查进度较慢，且参与者们对其整合的期待仍在持续。

#### 📝 邮件列表

1. **[05-06 15:47]** Re: [PATCH v21 0/4] arm64/perf: Enable branch stack sampling
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
2. **[05-06 16:30]** Re: [PATCH v21 0/4] arm64/perf: Enable branch stack sampling
   - 发件人: Rob Herring <robh@kernel.org>

---

### Thread 24: [PATCH] arm64: kvm: Replace ternary flags with str_on_off()
 helper

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 6 May 2025 11:34:16 +0800

#### 🤖 AI 总结

本邮件线程讨论的主题是一个针对 ARM64 KVM 的补丁，旨在用 `str_on_off()` 辅助函数替换三元标志。补丁的主要目的是提高代码的可读性和维护性。

在历史讨论中，补丁的提交者 Seongsu Park 提出了这个修改，并得到了 Zenghui Yu 的认可，表示已进行审核并标记为“Reviewed-by”。这表明补丁在技术上得到了初步的认可。

在本周的新讨论中，Zenghui Yu 建议将邮件主题修改为更清晰的格式，以便更好地反映补丁内容。Marc Zyngier 随后确认该补丁已被应用到 `kvm-arm64/misc-6.16` 分支，并表示感谢。这标志着该补丁的成功合并，进一步推动了 ARM64 KVM 的发展。

总的来说，本周的讨论主要集中在补丁的确认和合并上，反映出社区对代码质量和可读性的重视。

#### 📝 邮件列表

1. **[05-06 11:34]** Re: [PATCH] arm64: kvm: Replace ternary flags with str_on_off()
 helper
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>
2. **[05-06 09:39]** Re: [PATCH] arm64: kvm: Replace ternary flags with str_on_off() helper
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 25: [PATCH hyperv-next v9 00/11] arm64: hyperv: Support Virtual Trust Level Boot

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Apr 2025 14:07:31 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 ARM64 平台在 Hyper-V 中支持虚拟信任级别启动的补丁集，主题为“[PATCH hyperv-next v9 00/11] arm64: hyperv: Support Virtual Trust Level Boot”。

**原始补丁内容**：
该补丁集旨在使 Hyper-V 代码能够在 ARM64 架构下以虚拟信任级别（VTL）启动。虚拟信任级别是虚拟安全模式的一部分，相关文档可在 Microsoft 的 Top-Level Functional Specification 中找到。此外，OpenHCL paravisor 被提及为这些补丁在 ARM64 上的实际应用。

**之前讨论要点**：
在历史讨论中，Roman Kisel 提到该补丁集的验证工作，包括为不同架构和信任级别构建内核。虽然邮件内容较长，但主要集中在补丁的功能和验证上。

**本周新讨论进展**：
在本周的讨论中，Wei Liu 提到之前有多个评审意见，认为这些意见在当前版本中已得到解决。他对补丁的审查表示乐观，并已将整个补丁系列应用到 hyperv-next 分支。Wei 还邀请 ARM64 的维护者提出任何异议，如果有必要，他可以撤回该系列补丁，以便 Roman 处理进一步的评论。

总体来看，该补丁集在经过审查后，已准备好合并，期待 ARM64 维护者的反馈。

#### 📝 邮件列表

1. **[04-28 14:07]** [PATCH hyperv-next v9 00/11] arm64: hyperv: Support Virtual Trust Level Boot
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
2. **[05-06 06:19]** Re: [PATCH hyperv-next v9 00/11] arm64: hyperv: Support Virtual
 Trust Level Boot
   - 发件人: Wei Liu <wei.liu@kernel.org>

---

### Thread 26: [PATCH] KVM:FIXME comment is removed since no longer required

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  9 May 2025 15:29:57 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）中的一个代码补丁，主要内容是移除一个不再需要的 FIXME 注释。该补丁由 Pavan Bobba 提交，目的是简化代码，提升可读性。

在历史讨论中没有相关的背景信息，因此我们无法提供之前的讨论要点。本周的讨论中，Pavan Bobba 提出了该补丁，指出由于 `finalize_init_hyp_mode()` 函数在 `kvm_init()` 之后被调用，因此原有的 FIXME 注释已不再适用。补丁具体修改了 `arch/arm64/kvm/arm.c` 文件，删除了四行与 FIXME 注释相关的代码。

本周的进展主要集中在这一补丁的提交上，表明开发者在代码维护和清理方面的持续努力。没有其他参与者对此补丁进行讨论或提出意见。整体来看，此次补丁的提交是对 KVM 代码的一次小幅优化，旨在提高代码质量。

#### 📝 邮件列表

1. **[05-09 15:29]** [PATCH] KVM:FIXME comment is removed since no longer required
   - 发件人: Pavan Bobba <opensource206@gmail.com>

---

### Thread 27: [PATCH] KVM: selftests: add test for SVE host corruption

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue,  6 May 2025 09:51:54 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）中的自测试，具体是添加一个针对 SVE（Scalable Vector Extension）主机损坏的测试。

在本周的讨论中，Marc Zyngier 提到之前提交的补丁已经被应用到 kvm-arm64/misc-6.16 分支中。补丁的提交信息显示其主要目的是增加一个测试，以确保 SVE 功能在虚拟化环境下的稳定性和可靠性。

由于本周的邮件中没有提及之前的讨论内容，因此可以推测该补丁是基于对 SVE 主机损坏问题的关注而提出的，目的是增强 KVM 的自测试能力，确保在使用 SVE 时不会出现潜在的主机损坏问题。

总结来看，本周的进展是补丁成功应用，标志着对 KVM 中 SVE 功能的测试工作向前迈出了重要一步。

#### 📝 邮件列表

1. **[05-06 09:51]** Re: [PATCH] KVM: selftests: add test for SVE host corruption
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 Bug Report

共 1 个 thread

---

### Thread 1: [syzbot] [kvm?] [kvmarm?] BUG: unable to handle kernel paging request
 in vgic_its_save_tables_v0

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 09 May 2025 05:51:26 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的一个内核错误，具体表现为在 `vgic_its_save_tables_v0` 函数中无法处理内核分页请求。该问题由 syzbot 发现，并附上了相关的调试信息和重现步骤。

在历史讨论中并没有提供具体的补丁或之前的讨论内容，因此我们只能关注本周的新讨论。根据本周的邮件，syzbot 报告了一个内核错误，指出在尝试访问虚拟地址 `ffef80000000000001` 时发生了内存访问错误。报告中详细列出了错误信息，包括内存中断信息和调用栈，显示该错误与 `vgic_its_save_tables_v0` 函数的执行有关。

本周的讨论主要集中在该错误的具体表现和可能的原因上，syzbot 提供了详细的调试信息和重现步骤，便于开发者进行进一步的分析和修复。邮件中还提醒开发者在修复该问题后，需在提交的补丁中添加相应的报告标签，以便追踪问题的解决进展。

#### 📝 邮件列表

1. **[05-09 05:51]** [syzbot] [kvm?] [kvmarm?] BUG: unable to handle kernel paging request
 in vgic_its_save_tables_v0
   - 发件人: syzbot <syzbot+4ebd710a879482a93f8f@syzkaller.appspotmail.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.15, round #3

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 7 May 2025 00:55:44 -0700

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 在 Linux 6.15 版本中的修复补丁，属于第三轮更新。

1. **原始 patch/问题的内容**：本次补丁主要解决了多个与 KVM/arm64 相关的错误，包括修复 `user_mem_abort()` 中未初始化的内存缓存指针、确保在 VHE 模式下始终设置 HCR_EL2.xMO 位、阻止虚拟机监控器（VMM）隐藏 AArch64 支持等问题。此外，还修正了 `host_stage2_set_owner_locked()` 函数的内存检查逻辑。

2. **之前的讨论要点**：本次邮件没有提供历史讨论的具体内容，但从补丁内容来看，之前可能已经讨论过 KVM/arm64 的稳定性和功能性问题，尤其是在处理中断和内存管理方面。

3. **本周的新讨论、进展或结论**：本周的讨论主要由 Oliver Upton 提出，确认了这是针对 6.15 版本的最后一批修复，并强调了修复 `user_mem_abort()` 中的错误的重要性。Paolo Bonzini 对补丁表示认可并确认了处理。整体来看，补丁的提交和确认进展顺利，为即将发布的 6.15 版本提供了必要的修复。

#### 📝 邮件列表

1. **[05-07 00:55]** [GIT PULL] KVM/arm64 fixes for 6.15, round #3
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[05-10 17:10]** Re: [GIT PULL] KVM/arm64 fixes for 6.15, round #3
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Other

共 2 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v3 00/16] arm/arm64: Add kvmtool to the runner script

**📧 邮件数**: 36 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  7 May 2025 16:12:40 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 单元测试的补丁，主要集中在将 kvmtool 添加到测试运行脚本中，以支持 ARM 和 ARM64 架构的自动化测试。

1. **原始补丁内容**：补丁的目标是允许用户通过命令 `./configure --target=kvmtool` 和 `./run_tests.sh` 自动运行所有测试。kvmtool 相比于 QEMU 更小且更易于修改，能够更快地运行测试，但并非所有测试都能在 kvmtool 上运行。

2. **之前讨论要点**：历史讨论中提到，kvmtool 的命令行语法与 QEMU 不同，因此需要在测试定义中添加新的参数，如 `kvmtool_params`，以适应 kvmtool 的语法。此外，讨论了如何处理测试失败的情况，以及如何在使用 kvmtool 时避免不必要的错误。

3. **本周新讨论与进展**：本周的讨论中，参与者 Alexandru Elisei 提出了多个补丁，逐步实现 kvmtool 的支持，包括：重命名参数、添加 `test_args` 参数、导出 TARGET、文档更新、添加默认参数、支持 kvmtool 的运行等。最终，所有补丁都得到了 Andrew Jones 的审核和认可，确认了 kvmtool 的启用，并指出 EFI 测试仍不支持 kvmtool。

总之，本周的讨论和补丁更新使得 KVM 单元测试能够在 kvmtool 上运行，提升了测试的灵活性和效率。

#### 📝 邮件列表

1. **[05-07 16:12]** [kvm-unit-tests PATCH v3 00/16] arm/arm64: Add kvmtool to the runner script
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[05-07 16:12]** [kvm-unit-tests PATCH v3 01/16] scripts: unittests.cfg: Rename 'extra_params' to 'qemu_params'
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[05-07 16:12]** [kvm-unit-tests PATCH v3 02/16] scripts: Add 'test_args' test definition parameter
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
4. **[05-07 16:12]** [kvm-unit-tests PATCH v3 03/16] configure: Export TARGET unconditionally
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
5. **[05-07 16:12]** [kvm-unit-tests PATCH v3 04/16] run_tests.sh: Document --probe-maxsmp argument
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[05-07 16:12]** [kvm-unit-tests PATCH v3 05/16] scripts: Document environment variables
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
7. **[05-07 16:12]** [kvm-unit-tests PATCH v3 06/16] scripts: Refuse to run the tests if not configured for qemu
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
8. **[05-07 16:12]** [kvm-unit-tests PATCH v3 07/16] scripts: Use an associative array for qemu argument names
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
9. **[05-07 16:12]** [kvm-unit-tests PATCH v3 08/16] scripts: Add 'kvmtool_params' to test definition
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
10. **[05-07 16:12]** [kvm-unit-tests PATCH v3 09/16] scripts: Add support for kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
11. **[05-07 16:12]** [kvm-unit-tests PATCH v3 10/16] scripts: Add default arguments for kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
12. **[05-07 16:12]** [kvm-unit-tests PATCH v3 11/16] scripts: Add KVMTOOL environment variable for kvmtool binary path
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
13. **[05-07 16:12]** [kvm-unit-tests PATCH v3 12/16] scripts: Detect kvmtool failure in premature_failure()
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
14. **[05-07 16:12]** [kvm-unit-tests PATCH v3 13/16] scripts: Do not probe for maximum number of VCPUs when using kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
15. **[05-07 16:12]** [kvm-unit-tests PATCH v3 14/16] scripts/mkstandalone: Export $TARGET
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
16. **[05-07 16:12]** [kvm-unit-tests PATCH v3 15/16] scripts: Add 'disabled_if' test definition parameter for kvmtool to use
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
17. **[05-07 16:12]** [kvm-unit-tests PATCH v3 16/16] scripts: Enable kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
18. **[05-07 17:40]** Re: [kvm-unit-tests PATCH v3 01/16] scripts: unittests.cfg: Rename
 'extra_params' to 'qemu_params'
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
19. **[05-07 17:58]** Re: [kvm-unit-tests PATCH v3 02/16] scripts: Add 'test_args' test
 definition parameter
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
20. **[05-07 18:02]** Re: [kvm-unit-tests PATCH v3 03/16] configure: Export TARGET
 unconditionally
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
21. **[05-07 18:10]** Re: [kvm-unit-tests PATCH v3 06/16] scripts: Refuse to run the tests
 if not configured for qemu
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
22. **[05-07 17:14]** Re: [kvm-unit-tests PATCH v3 06/16] scripts: Refuse to run the tests
 if not configured for qemu
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
23. **[05-07 18:17]** Re: [kvm-unit-tests PATCH v3 07/16] scripts: Use an associative
 array for qemu argument names
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
24. **[05-07 18:28]** Re: [kvm-unit-tests PATCH v3 08/16] scripts: Add 'kvmtool_params' to
 test definition
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
25. **[05-07 18:38]** Re: [kvm-unit-tests PATCH v3 09/16] scripts: Add support for kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
26. **[05-07 18:43]** Re: [kvm-unit-tests PATCH v3 10/16] scripts: Add default arguments
 for kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
27. **[05-07 18:45]** Re: [kvm-unit-tests PATCH v3 11/16] scripts: Add KVMTOOL environment
 variable for kvmtool binary path
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
28. **[05-07 18:47]** Re: [kvm-unit-tests PATCH v3 12/16] scripts: Detect kvmtool failure
 in premature_failure()
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
29. **[05-07 18:48]** Re: [kvm-unit-tests PATCH v3 13/16] scripts: Do not probe for
 maximum number of VCPUs when using kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
30. **[05-07 18:56]** Re: [kvm-unit-tests PATCH v3 15/16] scripts: Add 'disabled_if' test
 definition parameter for kvmtool to use
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
31. **[05-07 18:59]** Re: [kvm-unit-tests PATCH v3 16/16] scripts: Enable kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
32. **[05-08 09:52]** Re: [kvm-unit-tests PATCH v3 03/16] configure: Export TARGET
 unconditionally
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
33. **[05-08 11:39]** Re: [kvm-unit-tests PATCH v3 03/16] configure: Export TARGET
 unconditionally
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
34. **[05-08 11:05]** Re: [kvm-unit-tests PATCH v3 03/16] configure: Export TARGET
 unconditionally
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
35. **[05-08 12:17]** Re: [kvm-unit-tests PATCH v3 03/16] configure: Export TARGET
 unconditionally
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
36. **[05-08 16:54]** Re: [kvm-unit-tests PATCH v3 08/16] scripts: Add 'kvmtool_params' to
 test definition
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 2: LM regression: fce886a60207 KVM: arm64: Plumb the pKVM MMU in KVM

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 5 May 2025 12:52:00 +0200 (CEST)

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的一个回归问题，具体涉及到提交的补丁 fce886a60207，该补丁旨在将 pKVM MMU 集成到 KVM 中。

在历史讨论中，参与者们并未提供具体的背景信息，但本周的讨论集中在一个具体问题上：在进行虚拟机迁移时，KVM_RUN 调用失败并返回 -ENOMEM 错误。Sebastian Ott 通过 Git bisect 确定了问题的根源是提交 fce886a60207，且在多次迁移后，KVM 在 ARM 设备上出现内存分配失败的情况。

本周的新讨论中，Sebastian 和 Marc Zyngier 进一步分析了导致 -ENOMEM 错误的原因，发现是由于在 `user_mem_abort()` 函数中，局部变量 memcache 的初始化条件不当，导致在某些情况下使用了未初始化的指针。Sebastian 提出了一个补丁，确保 memcache 始终有效，以解决迁移失败的问题。Marc 对补丁表示认可，并建议将其作为独立补丁提交，以便纳入下一个 6.15 版本的修复中。

总结来说，本周的讨论聚焦于解决 KVM 在 ARM64 上的迁移失败问题，提出了针对性的补丁，并达成了共识，期待尽快修复该问题。

#### 📝 邮件列表

1. **[05-05 12:52]** LM regression: fce886a60207 KVM: arm64: Plumb the pKVM MMU in KVM
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[05-05 12:34]** Re: LM regression: fce886a60207 KVM: arm64: Plumb the pKVM MMU in KVM
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[05-05 16:01]** Re: LM regression: fce886a60207 KVM: arm64: Plumb the pKVM MMU in
 KVM
   - 发件人: Sebastian Ott <sebott@redhat.com>
4. **[05-05 15:59]** Re: LM regression: fce886a60207 KVM: arm64: Plumb the pKVM MMU in KVM
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[05-05 18:05]** Re: LM regression: fce886a60207 KVM: arm64: Plumb the pKVM MMU in
 KVM
   - 发件人: Sebastian Ott <sebott@redhat.com>
6. **[05-05 17:26]** Re: LM regression: fce886a60207 KVM: arm64: Plumb the pKVM MMU in KVM
   - 发件人: Marc Zyngier <maz@kernel.org>

---

