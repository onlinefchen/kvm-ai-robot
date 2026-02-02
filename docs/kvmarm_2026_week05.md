# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2026-02-02 00:30:41

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 293
- **总 Thread 数**: 18
- **大型 Thread** (>20封): 5 个

### 分类分布

- **PATCH**: 18 threads (293 邮件)

---

## 📌 PATCH

共 18 个 thread

---

### Thread 1: [PATCH v10 00/30] Tracefs support for pKVM

**📧 邮件数**: 56 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 26 Jan 2026 10:43:49 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 的 Tracefs 支持的补丁（PATCH v10 00/30），主要集中在如何实现和改进虚拟化环境中的追踪功能。

1. **原始补丁内容**：
   - 该补丁系列引入了对 pKVM 的 Tracefs 支持，目的是为保护模式下的虚拟机监控器提供调试和分析工具。补丁包括创建远程事件和缓冲区的通用方法，并为 pKVM 超级监控器添加支持。

2. **历史讨论要点**：
   - 之前的讨论集中在如何设计和实现环形缓冲区、事件创建和 Tracefs 接口的细节。参与者们讨论了如何确保内核与虚拟机监控器之间的事件共享和同步。

3. **本周的新讨论和进展**：
   - 本周的讨论中，Vincent Donnefort 提出了多个补丁，涵盖了环形缓冲区的实现、Tracefs 远程支持、事件的创建和管理等。补丁中引入了新的宏和接口，以简化事件声明和处理。此外，Steven Rostedt 提出了代码审查意见，建议在某些情况下返回错误以防止不一致状态，并强调了文档和代码风格的一致性。最终，补丁得到了多位开发者的认可和审核通过。

总体来看，本周的讨论和补丁提交为 pKVM 的 Tracefs 支持奠定了基础，增强了虚拟化环境中的调试能力。

#### 📝 邮件列表

1. **[01-26 10:43]** [PATCH v10 00/30] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[01-26 10:43]** [PATCH v10 01/30] ring-buffer: Add page statistics to the meta-page
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[01-26 10:43]** [PATCH v10 02/30] ring-buffer: Store bpage pointers into subbuf_ids
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[01-26 10:43]** [PATCH v10 03/30] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[01-26 10:43]** [PATCH v10 04/30] ring-buffer: Add non-consuming read for ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[01-26 10:43]** [PATCH v10 05/30] tracing: Introduce trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[01-26 10:43]** [PATCH v10 06/30] tracing: Add reset to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[01-26 10:43]** [PATCH v10 07/30] tracing: Add non-consuming read to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[01-26 10:43]** [PATCH v10 08/30] tracing: Add init callback to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[01-26 10:43]** [PATCH v10 09/30] tracing: Add events to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[01-26 10:43]** [PATCH v10 10/30] tracing: Add events/ root files to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[01-26 10:44]** [PATCH v10 11/30] tracing: Add helpers to create trace remote events
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
13. **[01-26 10:44]** [PATCH v10 12/30] ring-buffer: Export buffer_data_page and macros
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
14. **[01-26 10:44]** [PATCH v10 13/30] tracing: Introduce simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
15. **[01-26 10:44]** [PATCH v10 14/30] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
16. **[01-26 10:44]** [PATCH v10 15/30] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
17. **[01-26 10:44]** [PATCH v10 16/30] Documentation: tracing: Add tracing remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
18. **[01-26 10:44]** [PATCH v10 17/30] tracing: load/unload page callbacks for simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
19. **[01-26 10:44]** [PATCH v10 18/30] tracing: Check for undefined symbols in simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
20. **[01-26 10:44]** [PATCH v10 19/30] KVM: arm64: Add PKVM_DISABLE_STAGE2_ON_PANIC
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
21. **[01-26 10:44]** [PATCH v10 20/30] KVM: arm64: Add clock support to nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
22. **[01-26 10:44]** [PATCH v10 21/30] KVM: arm64: Initialise hyp_nr_cpus for nVHE hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
23. **[01-26 10:44]** [PATCH v10 22/30] KVM: arm64: Support unaligned fixmap in the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
24. **[01-26 10:44]** [PATCH v10 23/30] KVM: arm64: Add tracing capability for the
 nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
25. **[01-26 10:44]** [PATCH v10 24/30] KVM: arm64: Add trace remote for the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
26. **[01-26 10:44]** [PATCH v10 25/30] KVM: arm64: Sync boot clock with the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
27. **[01-26 10:44]** [PATCH v10 26/30] KVM: arm64: Add trace reset to the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
28. **[01-26 10:44]** [PATCH v10 27/30] KVM: arm64: Add event support to the nVHE/pKVM hyp
 and trace remote
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
29. **[01-26 10:44]** [PATCH v10 28/30] KVM: arm64: Add hyp_enter/hyp_exit events to
 nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
30. **[01-26 10:44]** [PATCH v10 29/30] KVM: arm64: Add selftest event support to nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
31. **[01-26 10:44]** [PATCH v10 30/30] tracing: selftests: Add hypervisor trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
32. **[01-26 13:31]** Re: [PATCH v10 19/30] KVM: arm64: Add PKVM_DISABLE_STAGE2_ON_PANIC
   - 发件人: Kalesh Singh <kaleshsingh@google.com>
33. **[01-28 15:37]** Re: [PATCH v10 05/30] tracing: Introduce trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
34. **[01-28 15:52]** Re: [PATCH v10 05/30] tracing: Introduce trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
35. **[01-28 17:52]** Re: [PATCH v10 07/30] tracing: Add non-consuming read to trace
 remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
36. **[01-28 18:06]** Re: [PATCH v10 09/30] tracing: Add events to trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
37. **[01-28 18:18]** Re: [PATCH v10 13/30] tracing: Introduce simple_ring_buffer
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
38. **[01-28 19:25]** Re: [PATCH v10 01/30] ring-buffer: Add page statistics to the
 meta-page
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
39. **[01-28 19:26]** Re: [PATCH v10 02/30] ring-buffer: Store bpage pointers into
 subbuf_ids
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
40. **[01-28 19:26]** Re: [PATCH v10 03/30] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
41. **[01-28 19:26]** Re: [PATCH v10 04/30] ring-buffer: Add non-consuming read for
 ring-buffer remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
42. **[01-28 19:27]** Re: [PATCH v10 06/30] tracing: Add reset to trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
43. **[01-28 19:27]** Re: [PATCH v10 08/30] tracing: Add init callback to trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
44. **[01-28 19:28]** Re: [PATCH v10 10/30] tracing: Add events/ root files to trace
 remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
45. **[01-28 19:28]** Re: [PATCH v10 11/30] tracing: Add helpers to create trace remote
 events
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
46. **[01-28 19:28]** Re: [PATCH v10 12/30] ring-buffer: Export buffer_data_page and
 macros
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
47. **[01-29 11:34]** Re: [PATCH v10 14/30] tracing: Add a trace remote module for
 testing
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
48. **[01-29 12:05]** Re: [PATCH v10 15/30] tracing: selftests: Add trace remote tests
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
49. **[01-29 12:16]** Re: [PATCH v10 16/30] Documentation: tracing: Add tracing remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
50. **[01-29 12:21]** Re: [PATCH v10 17/30] tracing: load/unload page callbacks for
 simple_ring_buffer
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
51. **[01-29 12:33]** Re: [PATCH v10 18/30] tracing: Check for undefined symbols in
 simple_ring_buffer
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
52. **[01-29 12:37]** Re: [PATCH v10 00/30] Tracefs support for pKVM
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
53. **[01-29 21:34]** Re: [PATCH v10 00/30] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
54. **[01-29 21:39]** Re: [PATCH v10 05/30] tracing: Introduce trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
55. **[01-29 21:50]** Re: [PATCH v10 14/30] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
56. **[01-31 12:54]** Re: [PATCH v10 14/30] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 2: [PATCH 00/20] KVM: arm64: Generalise RESx handling

**📧 邮件数**: 50 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 26 Jan 2026 12:16:34 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 RESx（保留位）处理的改进，主要集中在 Marc Zyngier 提出的 20 个补丁上。

1. **原始补丁内容**：补丁系列旨在统一 RES0 和 RES1 位的处理，特别是针对 RES1 位的定义和管理。Marc 指出当前的 RES1 位处理存在不一致性，尤其是在 config.c 中的定义不明确，导致依赖于 FIXED_VALUE 等临时解决方案。

2. **之前讨论要点**：历史讨论中，Marc 提到需要清晰地定义缺失特性时的 RES1 位，并提出了使用统一数据结构来管理 RES0 和 RES1 位的想法。此外，补丁还包括对 SCTLR_EL2 的清理和调试功能的添加，以便于检查 RESx 设置。

3. **本周新讨论与进展**：本周的讨论主要集中在补丁的逐一审查和反馈上。Fuad Tabba 对多个补丁进行了审核，提出了一些代码风格和逻辑上的建议，认为新代码在逻辑上更清晰且易于理解。Marc 也回应了这些反馈，并表示将继续优化代码，确保补丁的逻辑清晰且符合规范。同时，补丁中还引入了新的调试文件，用于输出计算出的 RESx 值，以帮助验证其正确性。

总体而言，这一系列补丁旨在简化 KVM 在 arm64 架构下的 RESx 处理，提升代码的可读性和维护性，同时确保符合 ARM 架构规范。

#### 📝 邮件列表

1. **[01-26 12:16]** [PATCH 00/20] KVM: arm64: Generalise RESx handling
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[01-26 12:16]** [PATCH 01/20] arm64: Convert SCTLR_EL2 to sysreg infrastructure
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-26 12:16]** [PATCH 02/20] KVM: arm64: Remove duplicate configuration for SCTLR_EL1.{EE,E0E}
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[01-26 12:16]** [PATCH 03/20] KVM: arm64: Introduce standalone FGU computing primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[01-26 12:16]** [PATCH 04/20] KVM: arm64: Introduce data structure tracking both RES0 and RES1 bits
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[01-26 12:16]** [PATCH 05/20] KVM: arm64: Extend unified RESx handling to runtime sanitisation
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[01-26 12:16]** [PATCH 06/20] KVM: arm64: Inherit RESx bits from FGT register descriptors
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[01-26 12:16]** [PATCH 07/20] KVM: arm64: Allow RES1 bits to be inferred from configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[01-26 12:16]** [PATCH 08/20] KVM: arm64: Correctly handle SCTLR_EL1 RES1 bits for unsupported features
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[01-26 12:16]** [PATCH 09/20] KVM: arm64: Convert HCR_EL2.RW to AS_RES1
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[01-26 12:16]** [PATCH 10/20] KVM: arm64: Simplify FIXED_VALUE handling
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[01-26 12:16]** [PATCH 11/20] KVM: arm64: Add REQUIRES_E2H1 constraint as configuration flags
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[01-26 12:16]** [PATCH 12/20] KVM: arm64: Add RESx_WHEN_E2Hx constraints as configuration flags
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[01-26 12:16]** [PATCH 13/20] KVM: arm64: Move RESx into individual register descriptors
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[01-26 12:16]** [PATCH 14/20] KVM: arm64: Simplify handling of HCR_EL2.E2H RESx
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[01-26 12:16]** [PATCH 15/20] KVM: arm64: Get rid of FIXED_VALUE altogether
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[01-26 12:16]** [PATCH 16/20] KVM: arm64: Simplify handling of full register invalid constraint
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[01-26 12:16]** [PATCH 17/20] KVM: arm64: Remove all traces of FEAT_TME
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[01-26 12:16]** [PATCH 18/20] KVM: arm64: Remove all traces of HCR_EL2.MIOCNCE
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[01-26 12:16]** [PATCH 19/20] KVM: arm64: Add sanitisation to SCTLR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[01-26 12:16]** [PATCH 20/20] KVM: arm64: Add debugfs file dumping computed RESx values
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[01-26 17:53]** Re: [PATCH 01/20] arm64: Convert SCTLR_EL2 to sysreg infrastructure
   - 发件人: Fuad Tabba <tabba@google.com>
23. **[01-26 18:04]** Re: [PATCH 02/20] KVM: arm64: Remove duplicate configuration for SCTLR_EL1.{EE,E0E}
   - 发件人: Fuad Tabba <tabba@google.com>
24. **[01-26 18:35]** Re: [PATCH 03/20] KVM: arm64: Introduce standalone FGU computing primitive
   - 发件人: Fuad Tabba <tabba@google.com>
25. **[01-26 18:54]** Re: [PATCH 04/20] KVM: arm64: Introduce data structure tracking both
 RES0 and RES1 bits
   - 发件人: Fuad Tabba <tabba@google.com>
26. **[01-26 19:15]** Re: [PATCH 05/20] KVM: arm64: Extend unified RESx handling to runtime sanitisation
   - 发件人: Fuad Tabba <tabba@google.com>
27. **[01-27 10:52]** Re: [PATCH 05/20] KVM: arm64: Extend unified RESx handling to runtime sanitisation
   - 发件人: Marc Zyngier <maz@kernel.org>
28. **[01-27 15:21]** Re: [PATCH 06/20] KVM: arm64: Inherit RESx bits from FGT register
 descriptors
   - 发件人: Joey Gouly <joey.gouly@arm.com>
29. **[01-27 15:26]** Re: [PATCH 07/20] KVM: arm64: Allow RES1 bits to be inferred from
 configuration
   - 发件人: Joey Gouly <joey.gouly@arm.com>
30. **[01-27 17:58]** Re: [PATCH 06/20] KVM: arm64: Inherit RESx bits from FGT register descriptors
   - 发件人: Fuad Tabba <tabba@google.com>
31. **[01-27 17:58]** Re: [PATCH 07/20] KVM: arm64: Allow RES1 bits to be inferred from configuration
   - 发件人: Fuad Tabba <tabba@google.com>
32. **[01-27 18:06]** Re: [PATCH 08/20] KVM: arm64: Correctly handle SCTLR_EL1 RES1 bits
 for unsupported features
   - 发件人: Fuad Tabba <tabba@google.com>
33. **[01-27 18:09]** Re: [PATCH 09/20] KVM: arm64: Convert HCR_EL2.RW to AS_RES1
   - 发件人: Fuad Tabba <tabba@google.com>
34. **[01-27 18:20]** Re: [PATCH 10/20] KVM: arm64: Simplify FIXED_VALUE handling
   - 发件人: Fuad Tabba <tabba@google.com>
35. **[01-27 18:28]** Re: [PATCH 11/20] KVM: arm64: Add REQUIRES_E2H1 constraint as
 configuration flags
   - 发件人: Fuad Tabba <tabba@google.com>
36. **[01-28 17:43]** Re: [PATCH 12/20] KVM: arm64: Add RESx_WHEN_E2Hx constraints as
 configuration flags
   - 发件人: Fuad Tabba <tabba@google.com>
37. **[01-29 10:14]** Re: [PATCH 12/20] KVM: arm64: Add RESx_WHEN_E2Hx constraints as configuration flags
   - 发件人: Marc Zyngier <maz@kernel.org>
38. **[01-29 10:30]** Re: [PATCH 12/20] KVM: arm64: Add RESx_WHEN_E2Hx constraints as
 configuration flags
   - 发件人: Fuad Tabba <tabba@google.com>
39. **[01-29 16:29]** Re: [PATCH 13/20] KVM: arm64: Move RESx into individual register descriptors
   - 发件人: Fuad Tabba <tabba@google.com>
40. **[01-29 16:41]** Re: [PATCH 14/20] KVM: arm64: Simplify handling of HCR_EL2.E2H RESx
   - 发件人: Fuad Tabba <tabba@google.com>
41. **[01-29 16:54]** Re: [PATCH 15/20] KVM: arm64: Get rid of FIXED_VALUE altogether
   - 发件人: Fuad Tabba <tabba@google.com>
42. **[01-29 17:19]** Re: [PATCH 13/20] KVM: arm64: Move RESx into individual register descriptors
   - 发件人: Marc Zyngier <maz@kernel.org>
43. **[01-29 17:34]** Re: [PATCH 16/20] KVM: arm64: Simplify handling of full register
 invalid constraint
   - 发件人: Fuad Tabba <tabba@google.com>
44. **[01-29 17:39]** Re: [PATCH 13/20] KVM: arm64: Move RESx into individual register descriptors
   - 发件人: Fuad Tabba <tabba@google.com>
45. **[01-29 17:43]** Re: [PATCH 17/20] KVM: arm64: Remove all traces of FEAT_TME
   - 发件人: Fuad Tabba <tabba@google.com>
46. **[01-29 17:51]** Re: [PATCH 18/20] KVM: arm64: Remove all traces of HCR_EL2.MIOCNCE
   - 发件人: Fuad Tabba <tabba@google.com>
47. **[01-29 18:07]** Re: [PATCH 13/20] KVM: arm64: Move RESx into individual register descriptors
   - 发件人: Marc Zyngier <maz@kernel.org>
48. **[01-29 18:11]** Re: [PATCH 19/20] KVM: arm64: Add sanitisation to SCTLR_EL2
   - 发件人: Fuad Tabba <tabba@google.com>
49. **[01-29 18:13]** Re: [PATCH 13/20] KVM: arm64: Move RESx into individual register descriptors
   - 发件人: Fuad Tabba <tabba@google.com>
50. **[01-30 09:06]** Re: [PATCH 13/20] KVM: arm64: Move RESx into individual register descriptors
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 3: [PATCH v4 00/36] KVM: arm64: Introduce vGIC-v5 with PPI support

**📧 邮件数**: 49 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 28 Jan 2026 17:59:19 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 KVM 中引入对 GICv5 的支持，特别是针对 PPIs（私有中断）的实现和管理。

1. **原始 patch/问题的内容**：
   - 本次讨论的核心是引入 GICv5 设备的支持，特别是 PPIs 的管理。Sascha Bischoff 提出了一个补丁系列，旨在为 arm64 KVM 添加 GICv5 设备支持，初步实现了 PPI 的功能。

2. **之前讨论要点**：
   - 之前的讨论集中在 GICv5 的架构和如何在 KVM 中实现其功能。邮件中提到，GICv5 的设计使得大部分中断生命周期由硬件管理，减少了对每个 VCPU 的 AP 列表的需求。讨论还涉及了如何处理 PPI 的状态同步和中断注入。

3. **本周的新讨论、进展或结论**：
   - 本周的讨论中，Sascha 提出了多个补丁，涵盖了 GICv5 的初始化、PPIs 的状态管理、直接中断注入等功能。补丁中还引入了用户空间驱动的 PPI 掩码的 UAPI，以便用户空间能够查询可驱动的 PPIs。此外，讨论中提到，GICv5 不支持保护模式，因此在创建虚拟机时需要隐藏 GICv5 的相关功能。最终，Marc Zyngier 对补丁进行了审阅，并提出了一些建议和改进意见，确认了补丁的方向是正确的。

整体来看，本周的讨论和补丁推进了 KVM 对 GICv5 的支持，尤其是在 PPI 管理和中断处理方面，标志着 GICv5 功能的逐步完善。

#### 📝 邮件列表

1. **[01-28 17:59]** [PATCH v4 00/36] KVM: arm64: Introduce vGIC-v5 with PPI support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[01-28 17:59]** [PATCH v4 01/36] KVM: arm64: Account for RES1 bits in
 DECLARE_FEAT_MAP() and co
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[01-28 17:59]** [PATCH v4 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use generated
 ICH_VMCR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[01-28 18:00]** [PATCH v4 03/36] arm64/sysreg: Drop ICH_HFGRTR_EL2.ICC_HAPR_EL1 and
 make RES1
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[01-28 18:00]** [PATCH v4 04/36] arm64/sysreg: Add remaining GICv5 ICC_ & ICH_
 sysregs for KVM support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[01-28 18:00]** [PATCH v4 05/36] arm64/sysreg: Add GICR CDNMIA encoding
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
7. **[01-28 18:00]** [PATCH v4 06/36] KVM: arm64: gic: Set vgic_model before initing
 private IRQs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
8. **[01-28 18:01]** [PATCH v4 07/36] KVM: arm64: gic-v5: Add ARM_VGIC_V5 device to KVM
 headers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
9. **[01-28 18:01]** [PATCH v4 08/36] KVM: arm64: gic: Introduce interrupt type helpers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
10. **[01-28 18:01]** [PATCH v4 09/36] KVM: arm64: gic-v5: Add Arm copyright header
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
11. **[01-28 18:01]** [PATCH v4 10/36] KVM: arm64: gic-v5: Detect implemented PPIs on boot
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
12. **[01-28 18:02]** [PATCH v4 11/36] KVM: arm64: gic-v5: Sanitize ID_AA64PFR2_EL1.GCIE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
13. **[01-28 18:02]** [PATCH v4 12/36] KVM: arm64: gic-v5: Support GICv5 FGTs & FGUs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
14. **[01-28 18:02]** [PATCH v4 13/36] KVM: arm64: gic-v5: Add emulation for
 ICC_IAFFIDR_EL1 accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
15. **[01-28 18:02]** [PATCH v4 14/36] KVM: arm64: gic-v5: Add vgic-v5 save/restore hyp
 interface
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
16. **[01-28 18:03]** [PATCH v4 15/36] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
17. **[01-28 18:03]** [PATCH v4 16/36] KVM: arm64: gic-v5: Implement direct injection of
 PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
18. **[01-28 18:03]** [PATCH v4 17/36] KVM: arm64: gic-v5: Finalize GICv5 PPIs and generate
 mask
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
19. **[01-28 18:03]** [PATCH v4 18/36] KVM: arm64: gic: Introduce queue_irq_unlock to
 irq_ops
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
20. **[01-28 18:04]** [PATCH v4 19/36] KVM: arm64: gic-v5: Implement PPI interrupt
 injection
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
21. **[01-28 18:04]** [PATCH v4 20/36] KVM: arm64: gic-v5: Init Private IRQs (PPIs) for
 GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
22. **[01-28 18:04]** [PATCH v4 21/36] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
23. **[01-28 18:04]** [PATCH v4 22/36] KVM: arm64: gic-v5: Trap and mask guest
 ICC_PPI_ENABLERx_EL1 writes
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
24. **[01-28 18:05]** [PATCH v4 23/36] KVM: arm64: gic-v5: Support GICv5 interrupts with
 KVM_IRQ_LINE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
25. **[01-28 18:05]** [PATCH v4 24/36] KVM: arm64: gic-v5: Create and initialise vgic_v5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
26. **[01-28 18:05]** [PATCH v4 25/36] KVM: arm64: gic-v5: Reset vcpu state
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
27. **[01-28 18:06]** [PATCH v4 26/36] KVM: arm64: gic-v5: Bump arch timer for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
28. **[01-28 18:06]** [PATCH v4 27/36] KVM: arm64: gic-v5: Mandate architected PPI for PMU
 emulation on GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
29. **[01-28 18:06]** [PATCH v4 28/36] KVM: arm64: gic: Hide GICv5 for protected guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
30. **[01-28 18:06]** [PATCH v4 29/36] KVM: arm64: gic-v5: Hide FEAT_GCIE from NV GICv5
 guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
31. **[01-28 18:07]** [PATCH v4 30/36] KVM: arm64: gic-v5: Introduce kvm_arm_vgic_v5_ops
 and register them
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
32. **[01-28 18:07]** [PATCH v4 31/36] KVM: arm64: gic-v5: Set ICH_VCTLR_EL2.En on boot
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
33. **[01-28 18:07]** [PATCH v4 32/36] irqchip/gic-v5: Check if impl is virt capable
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
34. **[01-28 18:07]** [PATCH v4 33/36] KVM: arm64: gic-v5: Probe for GICv5 device
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
35. **[01-28 18:08]** [PATCH v4 34/36] Documentation: KVM: Introduce documentation for
 VGICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
36. **[01-28 18:08]** [PATCH v4 35/36] KVM: arm64: selftests: Introduce a minimal GICv5 PPI
 selftest
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
37. **[01-28 18:08]** [PATCH v4 36/36] KVM: arm64: gic-v5: Communicate userspace-driveable
 PPIs via a UAPI
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
38. **[01-29 12:29]** Re: [PATCH v4 35/36] KVM: arm64: selftests: Introduce a minimal
 GICv5 PPI selftest
   - 发件人: kernel test robot <lkp@intel.com>
39. **[01-29 12:15]** Re: [PATCH v4 10/36] KVM: arm64: gic-v5: Detect implemented PPIs on
 boot
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
40. **[01-29 12:21]** Re: [PATCH v4 21/36] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
41. **[01-29 12:25]** Re: [PATCH v4 36/36] KVM: arm64: gic-v5: Communicate
 userspace-driveable PPIs via a UAPI
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
42. **[01-30 11:03]** Re: [PATCH v4 10/36] KVM: arm64: gic-v5: Detect implemented PPIs on boot
   - 发件人: Marc Zyngier <maz@kernel.org>
43. **[01-30 11:14]** Re: [PATCH v4 32/36] irqchip/gic-v5: Check if impl is virt capable
   - 发件人: Marc Zyngier <maz@kernel.org>
44. **[01-30 11:18]** Re: (subset) [PATCH v4 00/36] KVM: arm64: Introduce vGIC-v5 with PPI support
   - 发件人: Marc Zyngier <maz@kernel.org>
45. **[01-30 11:38]** Re: [PATCH v4 11/36] KVM: arm64: gic-v5: Sanitize ID_AA64PFR2_EL1.GCIE
   - 发件人: Marc Zyngier <maz@kernel.org>
46. **[01-30 12:33]** Re: [PATCH v4 10/36] KVM: arm64: gic-v5: Detect implemented PPIs on
 boot
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
47. **[01-30 13:58]** Re: [PATCH v4 32/36] irqchip/gic-v5: Check if impl is virt capable
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
48. **[01-30 17:13]** Re: [PATCH v4 11/36] KVM: arm64: gic-v5: Sanitize
 ID_AA64PFR2_EL1.GCIE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
49. **[01-30 17:26]** Re: [PATCH v4 11/36] KVM: arm64: gic-v5: Sanitize ID_AA64PFR2_EL1.GCIE
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 4: [PATCH v3 00/47] arm_mpam: Add KVM/arm64 and resctrl glue code

**📧 邮件数**: 32 | **👥 参与者**: 8 | **📅 开始时间**: Mon, 12 Jan 2026 16:58:27 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM 架构的 MPAM（Memory Partitioning and Monitoring）功能的补丁系列，主要涉及 KVM/arm64 和 resctrl 的集成。原始补丁旨在添加 MPAM 的缺失部分，主要是小修正和代码整理，以便于在不同平台上进行测试和合并。

在历史讨论中，参与者探讨了 MPAM 的功能，包括如何在 SoC 中标记流量、缓存和带宽调节器的政策应用，以及如何处理 MPAM 注册表的上下文切换等技术细节。讨论中提到，MPAM 允许通过 PARTID 和 PMG 值来管理流量，并且与 x86 的类似功能（CLOSID 和 RMID）并不完全对应。

本周的新讨论中，Ben Horgan 提出了对 MPAM 默认设置的更新，以确保在启用 CDP（Cache Allocation Technology）时，所有 CPU 的默认值都能正确设置。此外，针对 MBW_MIN 和 MBW_MAX 的设置，Fenghua Yu 提出了将 MBW_MIN 默认设置为与 MBW_MAX 相等的建议，以避免在内存访问竞争时导致性能下降。Ben 也表示将删除某些补丁，并更新 MBW_MIN 的默认值，以便在未来更好地支持用户界面。

总体而言，讨论集中在如何优化 MPAM 功能以提高性能和兼容性，确保在不同硬件平台上能够有效运行。

#### 📝 邮件列表

1. **[01-12 16:58]** [PATCH v3 00/47] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[01-12 16:58]** [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[01-12 16:58]** [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[01-12 16:58]** [PATCH v3 29/47] arm_mpam: resctrl: Pick classes for use as mbm counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[01-12 16:59]** [PATCH v3 41/47] arm_mpam: Generate a configuration for min controls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[01-12 16:59]** [PATCH v3 45/47] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Ben Horgan <ben.horgan@arm.com>
7. **[01-13 15:39]** Re: [PATCH v3 41/47] arm_mpam: Generate a configuration for min
 controls
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
8. **[01-13 15:14]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
9. **[01-15 15:43]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
10. **[01-15 16:49]** Re: [PATCH v3 29/47] arm_mpam: resctrl: Pick classes for use as mbm counters
   - 发件人: Peter Newman <peternewman@google.com>
11. **[01-15 17:58]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
12. **[01-15 10:54]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
13. **[01-15 15:20]** Re: [PATCH v3 45/47] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Fenghua Yu <fenghuay@nvidia.com>
14. **[01-16 10:29]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
15. **[01-19 12:04]** Re: [PATCH v3 29/47] arm_mpam: resctrl: Pick classes for use as mbm
 counters
   - 发件人: James Morse <james.morse@arm.com>
16. **[01-19 12:23]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
17. **[01-19 13:47]** Re: [PATCH v3 29/47] arm_mpam: resctrl: Pick classes for use as mbm counters
   - 发件人: Peter Newman <peternewman@google.com>
18. **[01-19 20:56]** Re: [PATCH v3 45/47] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Ben Horgan <ben.horgan@arm.com>
19. **[01-20 16:28]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Peter Newman <peternewman@google.com>
20. **[01-21 09:58]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
21. **[01-23 14:29]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
22. **[01-26 14:30]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
23. **[01-26 14:50]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
24. **[01-26 16:00]** Re: [PATCH v3 29/47] arm_mpam: resctrl: Pick classes for use as mbm
 counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
25. **[01-29 14:14]** Re: [PATCH v3 45/47] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Fenghua Yu <fenghuay@nvidia.com>
26. **[01-30 11:07]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
27. **[01-30 11:19]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
28. **[01-30 12:21]** Re: [PATCH v3 45/47] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Ben Horgan <ben.horgan@arm.com>
29. **[01-30 14:04]** Re: [PATCH v3 29/47] arm_mpam: resctrl: Pick classes for use as mbm counters
   - 发件人: Peter Newman <peternewman@google.com>
30. **[01-30 14:17]** Re: [PATCH v3 41/47] arm_mpam: Generate a configuration for min
 controls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
31. **[01-30 14:38]** Re: [PATCH v3 29/47] arm_mpam: resctrl: Pick classes for use as mbm
 counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
32. **[01-30 20:30]** Re: [PATCH v3 41/47] arm_mpam: Generate a configuration for min
 controls
   - 发件人: Shanker Donthineni <sdonthineni@nvidia.com>

---

### Thread 5: [PATCH v11 00/30] Tracefs support for pKVM

**📧 邮件数**: 31 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 31 Jan 2026 13:28:18 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 的 Tracefs 支持的补丁系列（PATCH v11 00/30），主要集中在为 pKVM 超级管理程序添加调试和分析工具。以下是讨论的主要内容：

1. **原始补丁/问题的内容**：
   - 本补丁系列旨在为 pKVM 引入 Tracefs 支持，以便于调试和分析。Tracefs 提供了一个简单易用的接口，能够通过环形缓冲区在内核和超级管理程序之间共享跟踪事件。

2. **之前讨论的要点**：
   - 之前的讨论主要集中在如何实现环形缓冲区的远程事件和缓冲区的创建。补丁中引入了新的接口和数据结构，以支持远程写入和读取事件。

3. **本周的新讨论、进展或结论**：
   - 本周的讨论中，Vincent Donnefort 提出了多个补丁，涵盖了环形缓冲区的实现、Tracefs 目录的创建、事件的声明和处理等。补丁包括：
     - 引入简单环形缓冲区的实现，以便于 pKVM 超级管理程序使用。
     - 添加了 Tracefs 目录下的事件支持，使得可以通过 Tracefs 接口读取和控制远程跟踪缓冲区。
     - 讨论了如何在 nVHE/pKVM 超级管理程序中实现跟踪功能，包括跟踪时钟的同步、事件的创建和重置等。
     - 提供了自测事件的支持，以便进行 Tracefs 接口的自测。

整体来看，这一系列补丁的目标是增强 pKVM 的可调试性和可分析性，确保在使用 pKVM 时能够有效地记录和分析事件。

#### 📝 邮件列表

1. **[01-31 13:28]** [PATCH v11 00/30] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[01-31 13:28]** [PATCH v11 01/30] ring-buffer: Add page statistics to the meta-page
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[01-31 13:28]** [PATCH v11 02/30] ring-buffer: Store bpage pointers into subbuf_ids
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[01-31 13:28]** [PATCH v11 03/30] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[01-31 13:28]** [PATCH v11 04/30] ring-buffer: Add non-consuming read for ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[01-31 13:28]** [PATCH v11 05/30] tracing: Introduce trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[01-31 13:28]** [PATCH v11 06/30] tracing: Add reset to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[01-31 13:28]** [PATCH v11 07/30] tracing: Add non-consuming read to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[01-31 13:28]** [PATCH v11 08/30] tracing: Add init callback to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[01-31 13:28]** [PATCH v11 09/30] tracing: Add events to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[01-31 13:28]** [PATCH v11 10/30] tracing: Add events/ root files to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[01-31 13:28]** [PATCH v11 11/30] tracing: Add helpers to create trace remote events
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
13. **[01-31 13:28]** [PATCH v11 12/30] ring-buffer: Export buffer_data_page and macros
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
14. **[01-31 13:28]** [PATCH v11 13/30] tracing: Introduce simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
15. **[01-31 13:28]** [PATCH v11 14/30] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
16. **[01-31 13:28]** [PATCH v11 15/30] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
17. **[01-31 13:28]** [PATCH v11 16/30] Documentation: tracing: Add tracing remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
18. **[01-31 13:28]** [PATCH v11 17/30] tracing: load/unload page callbacks for simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
19. **[01-31 13:28]** [PATCH v11 18/30] tracing: Check for undefined symbols in simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
20. **[01-31 13:28]** [PATCH v11 19/30] KVM: arm64: Add PKVM_DISABLE_STAGE2_ON_PANIC
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
21. **[01-31 13:28]** [PATCH v11 20/30] KVM: arm64: Add clock support to nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
22. **[01-31 13:28]** [PATCH v11 21/30] KVM: arm64: Initialise hyp_nr_cpus for nVHE hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
23. **[01-31 13:28]** [PATCH v11 22/30] KVM: arm64: Support unaligned fixmap in the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
24. **[01-31 13:28]** [PATCH v11 23/30] KVM: arm64: Add tracing capability for the
 nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
25. **[01-31 13:28]** [PATCH v11 24/30] KVM: arm64: Add trace remote for the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
26. **[01-31 13:28]** [PATCH v11 25/30] KVM: arm64: Sync boot clock with the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
27. **[01-31 13:28]** [PATCH v11 26/30] KVM: arm64: Add trace reset to the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
28. **[01-31 13:28]** [PATCH v11 27/30] KVM: arm64: Add event support to the nVHE/pKVM hyp
 and trace remote
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
29. **[01-31 13:28]** [PATCH v11 28/30] KVM: arm64: Add hyp_enter/hyp_exit events to
 nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
30. **[01-31 13:28]** [PATCH v11 29/30] KVM: arm64: Add selftest event support to nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
31. **[01-31 13:28]** [PATCH v11 30/30] tracing: selftests: Add hypervisor trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 6: [PATCH v10 00/15] Direct Map Removal Support for guest_memfd

**📧 邮件数**: 17 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 26 Jan 2026 16:46:47 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 的 `guest_memfd` 功能的补丁系列，主要集中在移除直接映射支持的实现及其相关讨论。

1. **原始补丁内容**：
   本次补丁系列（PATCH v10 00/15）旨在为 `guest_memfd` 添加从主机内核的直接映射中移除虚拟机来宾内存的能力，以防止 Spectre 风格的瞬态执行问题。这一补丁扩展了 `guest_memfd` 的功能，使其能够在 KVM 来宾中实现更强的安全性。

2. **之前讨论要点**：
   之前的讨论主要集中在如何通过移除直接映射来增强安全性，尤其是针对潜在的 Spectre 攻击。补丁设计未发生实质性变化，主要进行了格式和错误处理的修复。

3. **本周的新讨论与进展**：
   本周的讨论中，补丁系列的多个部分被逐步提交，包括对 `set_memory` 函数的修改、引入新的辅助函数 `folio_zap_direct_map` 和 `folio_restore_direct_map`，以及对 GUEST_MEMFD_FLAG_NO_DIRECT_MAP 标志的支持。此外，针对 `guest_memfd` 的自测用例也得到了扩展，以验证在直接映射移除的情况下的功能。讨论中还提到了一些构建错误，开发者们正在积极修复这些问题。

总体来看，本周的讨论推动了 `guest_memfd` 功能的完善，特别是在安全性和自测方面的增强。

#### 📝 邮件列表

1. **[01-26 16:46]** [PATCH v10 00/15] Direct Map Removal Support for guest_memfd
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
2. **[01-26 16:46]** [PATCH v10 01/15] set_memory: set_direct_map_* to take address
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
3. **[01-26 16:47]** [PATCH v10 02/15] set_memory: add folio_{zap,restore}_direct_map
 helpers
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
4. **[01-26 16:47]** [PATCH v10 03/15] mm/gup: drop secretmem optimization from
 gup_fast_folio_allowed
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
5. **[01-26 16:47]** [PATCH v10 04/15] mm/gup: drop local variable in
 gup_fast_folio_allowed
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
6. **[01-26 16:47]** [PATCH v10 05/15] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
7. **[01-26 16:49]** [PATCH v10 06/15] KVM: guest_memfd: Add stub for
 kvm_arch_gmem_invalidate
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
8. **[01-26 16:50]** [PATCH v10 07/15] KVM: x86: define
 kvm_arch_gmem_supports_no_direct_map()
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
9. **[01-26 16:50]** [PATCH v10 08/15] KVM: arm64: define
 kvm_arch_gmem_supports_no_direct_map()
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
10. **[01-26 16:50]** [PATCH v10 09/15] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
11. **[01-26 16:50]** [PATCH v10 10/15] KVM: selftests: load elf via bounce buffer
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
12. **[01-26 16:50]** [PATCH v10 11/15] KVM: selftests: set KVM_MEM_GUEST_MEMFD in
 vm_mem_add() if guest_memfd != -1
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
13. **[01-26 16:53]** [PATCH v10 12/15] KVM: selftests: Add guest_memfd based
 vm_mem_backing_src_types
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
14. **[01-26 16:53]** [PATCH v10 13/15] KVM: selftests: cover
 GUEST_MEMFD_FLAG_NO_DIRECT_MAP in existing selftests
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
15. **[01-26 16:53]** [PATCH v10 14/15] KVM: selftests: stuff vm_mem_backing_src_type into
 vm_shape
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
16. **[01-26 16:53]** [PATCH v10 15/15] KVM: selftests: Test guest execution from direct
 map removed gmem
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
17. **[01-28 20:18]** Re: [PATCH v10 01/15] set_memory: set_direct_map_* to take address
   - 发件人: kernel test robot <lkp@intel.com>

---

### Thread 7: [PATCH v9 00/13] Direct Map Removal Support for guest_memfd

**📧 邮件数**: 15 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 14 Jan 2026 13:45:12 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个名为“直接映射移除支持”的补丁（PATCH v9 00/13），旨在增强虚拟机的内存安全性，防止类似Spectre的攻击。该补丁提出了一个新标志（GUEST_MEMFD_FLAG_NO_DIRECT_MAP），用于在创建guest_memfd时移除直接映射，以避免内核页表中包含指向虚拟机内存的条目，从而降低潜在的安全风险。

在历史讨论中，参与者探讨了该补丁的实现细节，特别是如何处理TDX虚拟机的直接映射问题。讨论中提到，TDX虚拟机的内存管理可能需要特殊处理，以避免因直接映射移除导致的崩溃或不稳定。

在本周的新讨论中，Nikita Kalyazin和Ackerley Tng对补丁的实现进行了进一步的澄清，确认在释放或转换folio时将其重新放回直接映射是足够的。同时，Rick Edgecombe提出了对功能进行拆分的建议，以简化补丁的复杂性，并确保在处理共享和私有页面时的安全性。整体来看，讨论朝着更清晰和安全的实现方向发展。

#### 📝 邮件列表

1. **[01-14 13:45]** [PATCH v9 00/13] Direct Map Removal Support for guest_memfd
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
2. **[01-14 13:46]** [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
3. **[01-15 23:04]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
4. **[01-16 00:00]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
5. **[01-16 15:00]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
6. **[01-16 09:30]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Vishal Annapurve <vannapurve@google.com>
7. **[01-16 17:51]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
8. **[01-22 08:44]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Ackerley Tng <ackerleytng@google.com>
9. **[01-22 17:35]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
10. **[01-22 10:37]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Ackerley Tng <ackerleytng@google.com>
11. **[01-22 14:47]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Ackerley Tng <ackerleytng@google.com>
12. **[01-23 00:01]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
13. **[01-26 16:56]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
14. **[01-27 16:21]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Ackerley Tng <ackerleytng@google.com>
15. **[01-27 16:29]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Ackerley Tng <ackerleytng@google.com>

---

### Thread 8: [PATCH kvmtool v5 0/7] arm64: Nested virtualization support

**📧 邮件数**: 12 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 23 Jan 2026 14:27:22 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 arm64 的嵌套虚拟化支持的补丁系列（PATCH kvmtool v5 0/7），主要集中在修复维护 IRQ 设置和处理 virtio 的字节序重置等问题。

**原始补丁内容**：
补丁系列的目标是为 arm64 架构添加嵌套虚拟化支持，修复了在某些维护 IRQ 设置失败时的边缘情况，并在未指定 `--nested` 选项时添加了警告。补丁中包括了对维护 IRQ 的设置支持、FEAT_E2H0 的支持以及 virtio 字节序的处理。

**之前讨论要点**：
在历史讨论中，参与者们讨论了补丁的实现细节和潜在的问题，例如如何正确设置维护 IRQ，以及在使用 EL2 转换机制时可能出现的错误。Marc Zyngier 和 Andre Przywara 之间的交流也涉及到对 GICv2 和 GICv3 的支持差异。

**本周新讨论与进展**：
本周的讨论中，Marc Zyngier 指出维护 IRQ 设置存在问题，并提出了修复建议。Sascha Bischoff 提出了对错误信息的改进建议，以便在使用不兼容的 GIC 版本时提供更明确的提示。Andre Przywara 对此表示同意，并讨论了在配置验证中添加更严格的检查的可能性。整体来看，参与者们在细节上进行了深入的交流，推动了补丁的完善。

#### 📝 邮件列表

1. **[01-23 14:27]** [PATCH kvmtool v5 0/7] arm64: Nested virtualization support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
2. **[01-23 14:27]** [PATCH kvmtool v5 3/7] arm64: nested: Add support for setting maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
3. **[01-23 14:27]** [PATCH kvmtool v5 5/7] arm64: Add FEAT_E2H0 support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
4. **[01-23 14:27]** [PATCH kvmtool v5 7/7] arm64: Handle virtio endianness reset when running nested
   - 发件人: Andre Przywara <andre.przywara@arm.com>
5. **[01-23 16:03]** Re: [PATCH kvmtool v5 7/7] arm64: Handle virtio endianness reset when running nested
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[01-26 18:03]** Re: [PATCH kvmtool v5 3/7] arm64: nested: Add support for setting maintenance IRQ
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[01-27 10:15]** Re: [PATCH kvmtool v5 7/7] arm64: Handle virtio endianness reset when
 running nested
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
8. **[01-27 12:07]** Re: [PATCH kvmtool v5 3/7] arm64: nested: Add support for setting
 maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
9. **[01-27 13:23]** Re: [PATCH kvmtool v5 3/7] arm64: nested: Add support for setting
 maintenance IRQ
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
10. **[01-29 18:08]** Re: [PATCH kvmtool v5 3/7] arm64: nested: Add support for setting
 maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
11. **[01-30 09:29]** Re: [PATCH kvmtool v5 3/7] arm64: nested: Add support for setting
 maintenance IRQ
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
12. **[01-30 09:29]** Re: [PATCH kvmtool v5 5/7] arm64: Add FEAT_E2H0 support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 9: [PATCH v3 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use
 generated ICH_VMCR_EL2

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 12 Jan 2026 14:00:07 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的 GIC（通用中断控制器）相关的补丁，特别是将 vGIC-v3 切换为使用生成的 ICH_VMCR_EL2 寄存器。

**原始补丁内容**：
补丁的目的是改进 vGIC-v3 的实现，使其使用生成的 ICH_VMCR_EL2 寄存器，以提高代码的可读性和维护性。

**之前讨论要点**：
在历史讨论中，参与者 Jonathan Cameron 对补丁提出了一些小的建议，尤其是关于使用 FIELD_PREP() 和 FIELD_GET() 的方式，虽然他表示对补丁的整体实现感到满意，并给予了“Reviewed-by”标记。讨论中还提到了一些其他补丁的细节，但主要集中在对 vGIC-v3 的实现上。

**本周新讨论进展**：
在本周的讨论中，Sascha Bischoff 对 Jonathan 的建议做出了回应，确认已将 FIELD_PREP() 添加到补丁中，以增强代码的清晰度。此外，Sascha 还提到在其他补丁中对代码进行了相应的调整，以便更好地使用 vgic_is_v5() 辅助函数。整体来看，本周的讨论主要集中在对补丁细节的确认和改进上，显示出参与者之间的良好协作。

#### 📝 邮件列表

1. **[01-12 14:00]** Re: [PATCH v3 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use
 generated ICH_VMCR_EL2
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
2. **[01-12 14:52]** Re: [PATCH v3 10/36] KVM: arm64: gic-v5: Detect implemented PPIs on
 boot
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
3. **[01-12 15:49]** Re: [PATCH v3 15/36] KVM: arm64: gic-v5: Implement GICv5 load/put
 and save/restore
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
4. **[01-28 17:26]** Re: [PATCH v3 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use
 generated ICH_VMCR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[01-28 17:28]** Re: [PATCH v3 10/36] KVM: arm64: gic-v5: Detect implemented PPIs on
 boot
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[01-28 17:31]** Re: [PATCH v3 15/36] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 10: [PATCH v2 1/5] arm64/sysreg: Add HDBSS related register information

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 22 Jan 2026 15:12:28 +0000

#### 🤖 AI 总结

在本邮件线程中，讨论的主题是关于为 arm64 架构添加与 HDBSS（Hybrid Dirty Bit Set）相关的寄存器信息的补丁（PATCH v2 1/5）。历史讨论中，Leonardo Bras 提到该补丁应基于 Marc Zyngier 提出的 VTCR_EL2 补丁进行重构，并表示自己正在利用该补丁集的特性进行新的优化工作。

在本周的新讨论中，Tian Zheng 确认将重构自己的补丁以适应 Marc 的工作，并确保 Leonardo 在下一次修订中被包含在抄送名单内。Leonardo 进一步指出，关于 KVM 的另一个补丁与 HDBSS 特性无关，建议将补丁系列拆分为两个部分：一个是为 KVM 启用 HAFDBS（Hybrid Address Format Dirty Bit Set），另一个是启用 HDBSS。他表示将提供一个示例作为基础。

Marc Zyngier 对于仅在 S2 启用脏位的做法表示反对，认为这在 KVM 中没有意义，强调 HDBSS 才是实现该功能的关键。因此，本周的讨论集中在补丁的重构和功能拆分上，以便更好地支持 HDBSS 特性。

#### 📝 邮件列表

1. **[01-22 15:12]** Re: [PATCH v2 1/5] arm64/sysreg: Add HDBSS related register information
   - 发件人: Leonardo Bras <leo.bras@arm.com>
2. **[01-26 10:21]** Re: [PATCH v2 1/5] arm64/sysreg: Add HDBSS related register
 information
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
3. **[01-26 11:50]** Re: [PATCH v2 1/5] arm64/sysreg: Add HDBSS related register information
   - 发件人: Leonardo Bras <leo.bras@arm.com>
4. **[01-29 17:02]** Re: [PATCH v2 2/5] KVM: arm64: Support set the DBM attr during memory abort
   - 发件人: Leonardo Bras <leo.bras@arm.com>
5. **[01-29 18:48]** Re: [PATCH v2 2/5] KVM: arm64: Support set the DBM attr during memory abort
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 11: [PATCH v2 00/35] KVM: arm64: Add support for protected guest memory with pKVM

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 19 Jan 2026 12:45:53 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下增加对受保护的来宾内存支持的补丁（PATCH v2 00/35），特别是通过 pKVM 实现的功能。

**原始补丁内容**：补丁系列的主要目标是增强 KVM 的安全性，允许来宾内存的保护。补丁中包括了对 `pkvm_handle_t` 类型的修改，将其从 32 位更改为 16 位，以便更好地与 pte 注释相结合。此外，还扩展了页面捐赠逻辑，以便在主机的 stage-2 页表中编码来宾句柄和 gfn（来宾物理页号）。

**之前讨论要点**：在历史讨论中，补丁的初步版本已经获得了一些反馈，导致增加了更多补丁以完善功能。补丁的设计考虑了超调用顺序的调整，以确保 pKVM 特定的调用在自己的范围内。

**本周的新讨论与进展**：在本周的讨论中，Fuad Tabba 对补丁 22 和 23 分别进行了审核，并表示通过。这表明补丁在社区中获得了认可，且向合并的方向迈出了重要一步。整体来看，补丁系列正在稳步推进，得到了积极的反馈。

#### 📝 邮件列表

1. **[01-19 12:45]** [PATCH v2 00/35] KVM: arm64: Add support for protected guest memory with pKVM
   - 发件人: Will Deacon <will@kernel.org>
2. **[01-19 12:46]** [PATCH v2 22/35] KVM: arm64: Change 'pkvm_handle_t' to u16
   - 发件人: Will Deacon <will@kernel.org>
3. **[01-19 12:46]** [PATCH v2 23/35] KVM: arm64: Annotate guest donations with handle and gfn in host stage-2
   - 发件人: Will Deacon <will@kernel.org>
4. **[01-28 10:28]** Re: [PATCH v2 22/35] KVM: arm64: Change 'pkvm_handle_t' to u16
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[01-28 10:29]** Re: [PATCH v2 23/35] KVM: arm64: Annotate guest donations with handle
 and gfn in host stage-2
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 12: [PATCH v12 06/46] arm64: RMI: Define the user ABI

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 23 Jan 2026 16:47:06 +0000

#### 🤖 AI 总结

在本次邮件讨论中，主题为“[PATCH v12 06/46] arm64: RMI: 定义用户 ABI”的补丁旨在明确用户空间与内核之间的接口（uABI），以便于更好地支持 ARM64 架构下的虚拟化。

**历史讨论**中，参与者探讨了补丁的结构和实现细节，Steven Price 提出了将相关实现补丁拆分的建议，以便更清晰地理解 uABI 的整体架构。此外，Suzuki K Poulose 讨论了调用限制，特别是关于内存区域的独立性和调用时机的问题。

**本周新讨论**中，Steven Price 回应了之前的讨论，强调保持补丁的完整性，以便于审查，并表示将进一步明确用户空间指针的含义。他提到，当前版本（RMM v1.0）存在一些问题，但在未来的 RMM v2.0 中将得到解决。此外，Steven 还提到未来可能会扩展 uAPI，以允许虚拟机监控器（VMM）更细粒度地控制 RIPAS 设置，但目前没有迫切的理由去实现这一点。

总体来看，讨论围绕着如何优化和扩展用户 ABI 接口，以支持更复杂的虚拟化需求，确保补丁在保持简洁的同时，能够提供有效的功能和安全性。

#### 📝 邮件列表

1. **[01-23 16:47]** Re: [PATCH v12 06/46] arm64: RMI: Define the user ABI
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
2. **[01-23 10:57]** Re: [PATCH v12 22/46] arm64: RMI: Create the realm descriptor
   - 发件人: Alper Gun <alpergun@google.com>
3. **[01-26 09:37]** Re: [PATCH v12 06/46] arm64: RMI: Define the user ABI
   - 发件人: Steven Price <steven.price@arm.com>
4. **[01-26 09:50]** Re: [PATCH v12 22/46] arm64: RMI: Create the realm descriptor
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 13: [PATCH v9 04/30] arm64/fpsimd: Check enable bit for FA64 when
 saving EFI state

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 29 Jan 2026 16:39:33 +0000

#### 🤖 AI 总结

本邮件线程讨论的是一个针对 ARM64 架构的补丁（PATCH v9 04/30），其内容是检查在保存 EFI 状态时 FA64 的使能位。该补丁旨在确保在处理浮点 SIMD 状态时能够正确管理 EFI 状态。

在历史讨论中，没有提供具体的背景信息，但本周的新讨论中，参与者 Alex Bennée 和 Mark Brown 讨论了该补丁与已合并的补丁 63de2b3859ba1 之间的冲突。Mark Brown 指出，由于该补丁与已合并的补丁存在冲突，因此建议将其删除。Alex Bennée 同意这一观点，并表示在下次重基时会将其去除。

此外，尽管该补丁需要删除，但讨论中提到的其他内容均可顺利应用，这表明整体进展是积极的。总的来说，本周的讨论集中在确认补丁的冲突和后续处理上。

#### 📝 邮件列表

1. **[01-29 16:39]** Re: [PATCH v9 04/30] arm64/fpsimd: Check enable bit for FA64 when
 saving EFI state
   - 发件人: =?utf-8?Q?Alex_Benn=C3=A9e?= <alex.bennee@linaro.org>
2. **[01-29 16:41]** Re: [PATCH v9 04/30] arm64/fpsimd: Check enable bit for FA64 when
 saving EFI state
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[01-29 17:29]** Re: [PATCH v9 04/30] arm64/fpsimd: Check enable bit for FA64 when
 saving EFI state
   - 发件人: =?utf-8?Q?Alex_Benn=C3=A9e?= <alex.bennee@linaro.org>

---

### Thread 14: [PATCH v1] KVM: selftests: Improve sea_to_user test

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 30 Jan 2026 19:28:37 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）自测试中的 `sea_to_user` 测试的改进。Jiaqi Yan 提交了一个补丁（PATCH v1），旨在改善该测试的多个方面，包括重构 `run_vm` 函数以捕获 GUEST_FAIL，确保测试在特定条件下正确退出，并添加关于虚拟机内存类型的注释。

在本周的讨论中，Jiaqi Yan 提出了补丁的具体改进内容，并展示了代码的修改，包括对错误处理的优化和注释的补充。然而，Marc Zyngier 对该测试的有效性表示了强烈的担忧，指出测试仍然存在严重问题，尤其是在权限要求和错误处理方面。他批评了测试中使用的嵌入式脚本方法，认为应直接在测试中驱动注入，而不是依赖 `popen()`。此外，他对测试的内存分配失败和对大页的依赖表示不满，认为这些问题使得测试不够健壮，甚至考虑在问题解决之前禁用该测试。

总体而言，本周的讨论集中在对补丁的反馈和对测试有效性的质疑上，反映出该测试在实现和设计上的不足之处。

#### 📝 邮件列表

1. **[01-30 19:28]** [PATCH v1] KVM: selftests: Improve sea_to_user test
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[01-31 12:37]** Re: [PATCH v1] KVM: selftests: Improve sea_to_user test
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 15: [PATCH] KVM: arm64: nv: Add trap config for DBGWCR<15>_EL1

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 30 Jan 2026 17:44:35 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主要是为 DBGWCR<15>_EL1 添加陷阱配置。

在本周的讨论中，Zenghui Yu 提出了一个补丁，指出在最初添加 MDCR_EL2 到陷阱转发基础设施时，DBGWCR<15>_EL1 的配置被遗漏了。补丁通过在 `emulate-nested.c` 文件中增加一行代码来修复这个问题，确保 DBGWCR<15>_EL1 能够正确地进行陷阱转发。

Marc Zyngier 对该补丁进行了快速响应，表示已将其应用到下一个版本中，并感谢 Zenghui Yu 的贡献。

总结而言，本周的讨论集中在补丁的提出和快速应用上，解决了之前遗漏的配置问题，进一步完善了 KVM 在 arm64 架构下的功能。

#### 📝 邮件列表

1. **[01-30 17:44]** [PATCH] KVM: arm64: nv: Add trap config for DBGWCR<15>_EL1
   - 发件人: Zenghui Yu <zenghui.yu@linux.dev>
2. **[01-30 10:00]** Re: [PATCH] KVM: arm64: nv: Add trap config for DBGWCR<15>_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 16: [PATCH] KVM: arm64: Fix various comments

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 28 Jan 2026 15:52:08 +0800

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的代码注释进行修正的补丁。补丁的主要内容包括将代码中的空格替换为制表符，并修正了两个小的拼写错误。具体修改涉及三个文件：`kvm_host.h`、`sysreg-sr.c` 和 `vgic-v3-nested.c`。

在之前的讨论中并没有提供具体的背景信息，邮件中仅包含了补丁的提交和相关修改内容的描述。

在本周的新讨论中，Zenghui Yu 提交了上述补丁，并得到了 Marc Zyngier 的确认和感谢，表示该补丁已被应用到下一个版本中。Marc Zyngier 提到补丁的提交哈希为 `82a32eacbacc6f7e372f98999e5ee1ee0dd7462d`，表明补丁已成功合并。

总结来看，本周的讨论主要集中在补丁的提交和确认上，未涉及其他技术细节或争议。

#### 📝 邮件列表

1. **[01-28 15:52]** [PATCH] KVM: arm64: Fix various comments
   - 发件人: Zenghui Yu <zenghui.yu@linux.dev>
2. **[01-30 09:59]** Re: [PATCH] KVM: arm64: Fix various comments
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 17: [PATCH 0/3] KVM: arm64: Reschedule as needed when destroying the stage-2 page-tables

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 28 Jan 2026 16:47:48 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理阶段 2 页表销毁时的调度问题。原始的补丁（PATCH 0/3）旨在在销毁阶段 2 页表时，根据需要进行重新调度，以提高系统的稳定性和性能。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了优化 KVM 在处理虚拟机时的内存管理，特别是在销毁页表的过程中，可能会影响到虚拟机的正常运行。

在本周的新讨论中，Marc Zyngier 提出了对该补丁的担忧，指出它可能会严重影响其 NV（Nested Virtualization）虚拟机的运行，导致 L2 和 L3 虚拟机卡死，而 L0 和 L1 虚拟机则在处理阶段 2 页表时出现问题。他怀疑这是由于 TLB（Translation Lookaside Buffer）失效处理不当所导致的，可能会进一步影响 S2 管理的稳定性。Marc 还提到该问题在 M2 和 QC 机器上均可重现，显示出补丁可能存在广泛的影响。

总结而言，该补丁的初衷是优化虚拟化管理，但目前的反馈显示其可能引发严重的兼容性问题，需进一步调查和修正。

#### 📝 邮件列表

1. **[01-28 16:47]** Re: [PATCH 0/3] KVM: arm64: Reschedule as needed when destroying the stage-2 page-tables
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 18: [PATCH 0/2] Enable GICv5 Legacy CPUIF trapping & fix TDIR cap test

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 27 Jan 2026 14:09:03 +0000

#### 🤖 AI 总结

本邮件讨论主题为“启用 GICv5 传统 CPUIF 捕获及修复 TDIR 能力测试”，包含两个补丁（patch）。第一个补丁旨在在 GICv5 主机上启用 GICv3 CPUIF 捕获，第二个补丁则修正了针对 GICv5 主机的 ICH_HCR_EL2_TDIR 能力测试。

在历史讨论中，虽然没有详细记录，但可以推测之前的讨论涉及 GICv5 的功能实现及其对 KVM（Kernel-based Virtual Machine）的支持，特别是 CPUIF 捕获的必要性和能力测试的准确性。

在本周的新讨论中，Marc Zyngier 确认这两个补丁已被应用到下一步的开发中，并感谢 Sascha Bischoff 的贡献。这表明补丁已获得认可并将继续推进，标志着对 GICv5 支持的进一步完善。整体来看，本周的讨论主要集中在补丁的应用和后续工作安排上。

#### 📝 邮件列表

1. **[01-27 14:09]** Re: [PATCH 0/2] Enable GICv5 Legacy CPUIF trapping & fix TDIR cap test
   - 发件人: Marc Zyngier <maz@kernel.org>

---

