# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-12-08 00:24:22

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 199
- **总 Thread 数**: 29
- **大型 Thread** (>20封): 3 个

### 分类分布

- **PATCH**: 19 threads (167 邮件)
- **Selftest**: 1 threads (3 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Discussion**: 7 threads (12 邮件)
- **Other**: 1 threads (15 邮件)

---

## 📌 PATCH

共 19 个 thread

---

### Thread 1: [PATCH v6 00/44] KVM: x86: Add support for mediated vPMUs

**📧 邮件数**: 45 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  5 Dec 2025 16:16:36 -0800

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）对中介虚拟性能监控单元（mediated vPMUs）的支持，主要内容涵盖了多个补丁（patch）的提交和讨论。

1. **原始 Patch/问题的内容**：
   本次补丁系列的核心是为 KVM x86 添加对中介 vPMU 的支持，允许虚拟机直接访问硬件性能监控单元（PMU），而不需要通过 KVM 进行代理。这种方法旨在提高虚拟机的性能监控精度和效率。

2. **之前讨论要点**：
   在之前的讨论中，参与者们探讨了中介 vPMU 的实现细节，包括如何在虚拟机上下文切换时处理 PMU 状态、如何管理与性能监控相关的 MSR（模型特定寄存器）拦截，以及如何确保在虚拟机运行时不会影响宿主机的性能监控。

3. **本周的新讨论、进展或结论**：
   - 本周的讨论集中在多个补丁的提交上，包括对中介 PMU 的加载和保存机制、MSR 拦截的调整、以及如何在虚拟机进入和退出时管理 PMU 状态。
   - 具体补丁包括：优化了对 PMU 事件选择器的管理，确保在虚拟机上下文切换时能够正确处理 PMU 计数器的状态；引入了新的 API 以支持中介 PMU 的创建和释放；并且在处理 PMU 相关的 MSR 时，确保了宿主机和虚拟机之间的状态一致性。
   - 讨论中还提到需要对用户空间暴露中介 PMU 的支持参数，以便用户可以根据需求启用或禁用该功能。

整体而言，本周的讨论和补丁提交进一步推进了 KVM 对中介 vPMU 支持的实现，旨在提高虚拟化环境下的性能监控能力。

#### 📝 邮件列表

1. **[12-05 16:16]** [PATCH v6 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[12-05 16:16]** [PATCH v6 01/44] perf: Skip pmu_ctx based on event_type
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[12-05 16:16]** [PATCH v6 02/44] perf: Add generic exclude_guest support
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[12-05 16:16]** [PATCH v6 03/44] perf: Move security_perf_event_free() call to __free_event()
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[12-05 16:16]** [PATCH v6 04/44] perf: Add APIs to create/release mediated guest vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[12-05 16:16]** [PATCH v6 05/44] perf: Clean up perf ctx time
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[12-05 16:16]** [PATCH v6 06/44] perf: Add a EVENT_GUEST flag
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[12-05 16:16]** [PATCH v6 07/44] perf: Add APIs to load/put guest mediated PMU context
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[12-05 16:16]** [PATCH v6 08/44] perf/x86/core: Register a new vector for handling
 mediated guest PMIs
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[12-05 16:16]** [PATCH v6 09/44] perf/x86/core: Add APIs to switch to/from mediated
 PMI vector (for KVM)
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[12-05 16:16]** [PATCH v6 10/44] perf/x86/core: Do not set bit width for unavailable counters
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[12-05 16:16]** [PATCH v6 11/44] perf/x86/core: Plumb mediated PMU capability from
 x86_pmu to x86_pmu_cap
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[12-05 16:16]** [PATCH v6 12/44] perf/x86/intel: Support PERF_PMU_CAP_MEDIATED_VPMU
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[12-05 16:16]** [PATCH v6 13/44] perf/x86/amd: Support PERF_PMU_CAP_MEDIATED_VPMU for
 AMD host
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[12-05 16:16]** [PATCH v6 14/44] KVM: Add a simplified wrapper for registering perf callbacks
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[12-05 16:16]** [PATCH v6 15/44] KVM: x86/pmu: Snapshot host (i.e. perf's) reported
 PMU capabilities
   - 发件人: Sean Christopherson <seanjc@google.com>
17. **[12-05 16:16]** [PATCH v6 16/44] KVM: x86/pmu: Start stubbing in mediated PMU support
   - 发件人: Sean Christopherson <seanjc@google.com>
18. **[12-05 16:16]** [PATCH v6 17/44] KVM: x86/pmu: Implement Intel mediated PMU
 requirements and constraints
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[12-05 16:16]** [PATCH v6 18/44] KVM: x86/pmu: Implement AMD mediated PMU requirements
   - 发件人: Sean Christopherson <seanjc@google.com>
20. **[12-05 16:16]** [PATCH v6 19/44] KVM: x86/pmu: Register PMI handler for mediated vPMU
   - 发件人: Sean Christopherson <seanjc@google.com>
21. **[12-05 16:16]** [PATCH v6 20/44] KVM: x86/pmu: Disable RDPMC interception for
 compatible mediated vPMU
   - 发件人: Sean Christopherson <seanjc@google.com>
22. **[12-05 16:16]** [PATCH v6 21/44] KVM: x86/pmu: Load/save GLOBAL_CTRL via entry/exit
 fields for mediated PMU
   - 发件人: Sean Christopherson <seanjc@google.com>
23. **[12-05 16:16]** [PATCH v6 22/44] KVM: x86/pmu: Disable interception of select PMU
 MSRs for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
24. **[12-05 16:16]** [PATCH v6 23/44] KVM: x86/pmu: Bypass perf checks when emulating
 mediated PMU counter accesses
   - 发件人: Sean Christopherson <seanjc@google.com>
25. **[12-05 16:17]** [PATCH v6 24/44] KVM: x86/pmu: Introduce eventsel_hw to prepare for
 pmu event filtering
   - 发件人: Sean Christopherson <seanjc@google.com>
26. **[12-05 16:17]** [PATCH v6 25/44] KVM: x86/pmu: Reprogram mediated PMU event selectors
 on event filter updates
   - 发件人: Sean Christopherson <seanjc@google.com>
27. **[12-05 16:17]** [PATCH v6 26/44] KVM: x86/pmu: Always stuff GuestOnly=1,HostOnly=0
 for mediated PMCs on AMD
   - 发件人: Sean Christopherson <seanjc@google.com>
28. **[12-05 16:17]** [PATCH v6 27/44] KVM: x86/pmu: Load/put mediated PMU context when
 entering/exiting guest
   - 发件人: Sean Christopherson <seanjc@google.com>
29. **[12-05 16:17]** [PATCH v6 28/44] KVM: x86/pmu: Disallow emulation in the fastpath if
 mediated PMCs are active
   - 发件人: Sean Christopherson <seanjc@google.com>
30. **[12-05 16:17]** [PATCH v6 29/44] KVM: x86/pmu: Handle emulated instruction for
 mediated vPMU
   - 发件人: Sean Christopherson <seanjc@google.com>
31. **[12-05 16:17]** [PATCH v6 30/44] KVM: nVMX: Add macros to simplify nested MSR
 interception setting
   - 发件人: Sean Christopherson <seanjc@google.com>
32. **[12-05 16:17]** [PATCH v6 31/44] KVM: nVMX: Disable PMU MSR interception as
 appropriate while running L2
   - 发件人: Sean Christopherson <seanjc@google.com>
33. **[12-05 16:17]** [PATCH v6 32/44] KVM: nSVM: Disable PMU MSR interception as
 appropriate while running L2
   - 发件人: Sean Christopherson <seanjc@google.com>
34. **[12-05 16:17]** [PATCH v6 33/44] KVM: x86/pmu: Expose enable_mediated_pmu parameter
 to user space
   - 发件人: Sean Christopherson <seanjc@google.com>
35. **[12-05 16:17]** [PATCH v6 34/44] KVM: x86/pmu: Elide WRMSRs when loading guest PMCs
 if values already match
   - 发件人: Sean Christopherson <seanjc@google.com>
36. **[12-05 16:17]** [PATCH v6 35/44] KVM: VMX: Drop intermediate "guest" field from msr_autostore
   - 发件人: Sean Christopherson <seanjc@google.com>
37. **[12-05 16:17]** [PATCH v6 36/44] KVM: nVMX: Don't update msr_autostore count when
 saving TSC for vmcs12
   - 发件人: Sean Christopherson <seanjc@google.com>
38. **[12-05 16:17]** [PATCH v6 37/44] KVM: VMX: Dedup code for removing MSR from VMCS's
 auto-load list
   - 发件人: Sean Christopherson <seanjc@google.com>
39. **[12-05 16:17]** [PATCH v6 38/44] KVM: VMX: Drop unused @entry_only param from add_atomic_switch_msr()
   - 发件人: Sean Christopherson <seanjc@google.com>
40. **[12-05 16:17]** [PATCH v6 39/44] KVM: VMX: Bug the VM if either MSR auto-load list is full
   - 发件人: Sean Christopherson <seanjc@google.com>
41. **[12-05 16:17]** [PATCH v6 40/44] KVM: VMX: Set MSR index auto-load entry if and only
 if entry is "new"
   - 发件人: Sean Christopherson <seanjc@google.com>
42. **[12-05 16:17]** [PATCH v6 41/44] KVM: VMX: Compartmentalize adding MSRs to host vs.
 guest auto-load list
   - 发件人: Sean Christopherson <seanjc@google.com>
43. **[12-05 16:17]** [PATCH v6 42/44] KVM: VMX: Dedup code for adding MSR to VMCS's auto list
   - 发件人: Sean Christopherson <seanjc@google.com>
44. **[12-05 16:17]** [PATCH v6 43/44] KVM: VMX: Initialize vmcs01.VM_EXIT_MSR_STORE_ADDR
 with list address
   - 发件人: Sean Christopherson <seanjc@google.com>
45. **[12-05 16:17]** [PATCH v6 44/44] KVM: VMX: Add mediated PMU support for CPUs without
 "save perf global ctrl"
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 2: [PATCH v9 00/30] Tracefs support for pKVM

**📧 邮件数**: 31 | **👥 参与者**: 1 | **📅 开始时间**: Tue,  2 Dec 2025 09:35:53 +0000

#### 🤖 AI 总结

本邮件列表讨论的主题是针对 pKVM 的 Tracefs 支持的补丁系列（[PATCH v9 00/30]）。该补丁旨在为 pKVM 超级管理程序引入调试和分析工具，主要通过 Tracefs 实现。

**原始补丁内容**：
补丁系列的核心是引入了一种新的通用方式来创建远程事件和远程缓冲区，并为 pKVM 超级管理程序添加支持。补丁中包括了环形缓冲区的设置、Tracefs 的集成、简单环形缓冲区的实现、事件的创建宏等。

**历史讨论要点**：
在之前的讨论中，参与者强调了 Tracefs 的易用性和脚本化能力，认为其适合用于调试和性能分析。补丁的设计考虑到了与现有工具的兼容性，并提供了一种新的接口来处理远程写入和读取事件。

**本周新讨论及进展**：
本周的讨论集中在补丁的具体实现上，包括：
1. 添加了对环形缓冲区的页面统计信息支持。
2. 引入了简单环形缓冲区的实现，旨在减少对 pKVM 超级管理程序的依赖。
3. 实现了 Tracefs 目录结构，以支持远程事件的创建和管理。
4. 进行了自测模块的开发，以验证 Tracefs 支持的正确性。
5. 讨论了如何在 nVHE 模式下同步引导时钟，以及如何在 pKVM 超级管理程序中实现事件支持。

总结而言，该补丁系列的目标是通过 Tracefs 提供强大的调试和分析能力，以支持 pKVM 超级管理程序的开发和维护。

#### 📝 邮件列表

1. **[12-02 09:35]** [PATCH v9 00/30] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[12-02 09:35]** [PATCH v9 01/30] ring-buffer: Add page statistics to the meta-page
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[12-02 09:35]** [PATCH v9 02/30] ring-buffer: Store bpage pointers into subbuf_ids
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[12-02 09:35]** [PATCH v9 03/30] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[12-02 09:35]** [PATCH v9 04/30] ring-buffer: Add non-consuming read for ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[12-02 09:35]** [PATCH v9 05/30] tracing: Introduce trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[12-02 09:35]** [PATCH v9 06/30] tracing: Add reset to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[12-02 09:36]** [PATCH v9 07/30] tracing: Add non-consuming read to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[12-02 09:36]** [PATCH v9 08/30] tracing: Add init callback to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[12-02 09:36]** [PATCH v9 09/30] tracing: Add events to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[12-02 09:36]** [PATCH v9 10/30] tracing: Add events/ root files to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[12-02 09:36]** [PATCH v9 11/30] tracing: Add helpers to create trace remote events
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
13. **[12-02 09:36]** [PATCH v9 12/30] ring-buffer: Export buffer_data_page and macros
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
14. **[12-02 09:36]** [PATCH v9 13/30] tracing: Introduce simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
15. **[12-02 09:36]** [PATCH v9 14/30] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
16. **[12-02 09:36]** [PATCH v9 15/30] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
17. **[12-02 09:36]** [PATCH v9 16/30] Documentation: tracing: Add tracing remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
18. **[12-02 09:36]** [PATCH v9 17/30] tracing: load/unload page callbacks for simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
19. **[12-02 09:36]** [PATCH v9 18/30] tracing: Check for undefined symbols in simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
20. **[12-02 09:36]** [PATCH v9 19/30] KVM: arm64: Add PKVM_DISABLE_STAGE2_ON_PANIC
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
21. **[12-02 09:36]** [PATCH v9 20/30] KVM: arm64: Add clock support to nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
22. **[12-02 09:36]** [PATCH v9 21/30] KVM: arm64: Initialise hyp_nr_cpus for nVHE hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
23. **[12-02 09:36]** [PATCH v9 22/30] KVM: arm64: Support unaligned fixmap in the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
24. **[12-02 09:36]** [PATCH v9 23/30] KVM: arm64: Add tracing capability for the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
25. **[12-02 09:36]** [PATCH v9 24/30] KVM: arm64: Add trace remote for the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
26. **[12-02 09:36]** [PATCH v9 25/30] KVM: arm64: Sync boot clock with the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
27. **[12-02 09:36]** [PATCH v9 26/30] KVM: arm64: Add trace reset to the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
28. **[12-02 09:36]** [PATCH v9 27/30] KVM: arm64: Add event support to the nVHE/pKVM hyp
 and trace remote
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
29. **[12-02 09:36]** [PATCH v9 28/30] KVM: arm64: Add hyp_enter/hyp_exit events to
 nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
30. **[12-02 09:36]** [PATCH v9 29/30] KVM: arm64: Add selftest event support to nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
31. **[12-02 09:36]** [PATCH v9 30/30] tracing: selftests: Add hypervisor trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 3: [PATCH v3 0/9] KVM: arm64: Add support for FEAT_IDST

**📧 邮件数**: 21 | **👥 参与者**: 4 | **📅 开始时间**: Thu,  4 Dec 2025 09:47:57 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FEAT_IDST（ARMv8.4 引入的特性）的补丁系列。该特性允许在未实现的情况下捕获 ID 寄存器的访问，涉及 GMID_EL1、CCSIDR2_EL1 和 SMIDR_EL1 三个寄存器。

在历史讨论中，Marc Zyngier 提出了该补丁系列的初步版本，主要目标是通过特定方式处理这三个寄存器，并在过程中实现 GMID_EL1 的支持。补丁系列经过多次修改，增强了对寄存器的通用处理，并引入了自测试以验证功能。

本周的新讨论中，Marc 提交了补丁的第 3 到第 9 个版本，具体包括：
1. 增强了对 GMID_EL1 的捕获路由支持。
2. 引入了通用的同步异常注入原语，简化了异常处理。
3. 处理了没有特定处理程序的系统寄存器，确保符合 FEAT_IDST 的语义。
4. 通过自测试验证 FEAT_IDST 的功能是否正常。

参与者对补丁进行了审查和讨论，提出了一些改进建议，整体进展顺利，补丁得到了多个参与者的认可。

#### 📝 邮件列表

1. **[12-04 09:47]** [PATCH v3 0/9] KVM: arm64: Add support for FEAT_IDST
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[12-04 09:47]** [PATCH v3 1/9] arm64: Repaint ID_AA64MMFR2_EL1.IDS description
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[12-04 09:47]** [PATCH v3 2/9] KVM: arm64: Add trap routing for GMID_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[12-04 09:48]** [PATCH v3 3/9] KVM: arm64: Add a generic synchronous exception injection primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[12-04 09:48]** [PATCH v3 4/9] KVM: arm64: Handle FEAT_IDST for sysregs without specific handlers
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[12-04 09:48]** [PATCH v3 5/9] KVM: arm64: Handle CSSIDR2_EL1 and SMIDR_EL1 in a generic way
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[12-04 09:48]** [PATCH v3 6/9] KVM: arm64: Force trap of GMID_EL1 when the guest doesn't have MTE
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[12-04 09:48]** [PATCH v3 7/9] KVM: arm64: pkvm: Add a generic synchronous exception injection primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[12-04 09:48]** [PATCH v3 8/9] KVM: arm64: pkvm: Report optional ID register traps with a 0x18 syndrome
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[12-04 09:48]** [PATCH v3 9/9] KVM: arm64: selftests: Add a test for FEAT_IDST
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[12-04 10:32]** Re: [PATCH v3 1/9] arm64: Repaint ID_AA64MMFR2_EL1.IDS description
   - 发件人: Joey Gouly <joey.gouly@arm.com>
12. **[12-04 10:36]** Re: [PATCH v3 1/9] arm64: Repaint ID_AA64MMFR2_EL1.IDS description
   - 发件人: Ben Horgan <ben.horgan@arm.com>
13. **[12-04 10:48]** Re: [PATCH v3 1/9] arm64: Repaint ID_AA64MMFR2_EL1.IDS description
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[12-04 10:51]** Re: [PATCH v3 8/9] KVM: arm64: pkvm: Report optional ID register
 traps with a 0x18 syndrome
   - 发件人: Ben Horgan <ben.horgan@arm.com>
15. **[12-04 10:52]** Re: [PATCH v3 4/9] KVM: arm64: Handle FEAT_IDST for sysregs without
 specific handlers
   - 发件人: Joey Gouly <joey.gouly@arm.com>
16. **[12-04 11:13]** Re: [PATCH v3 1/9] arm64: Repaint ID_AA64MMFR2_EL1.IDS description
   - 发件人: Ben Horgan <ben.horgan@arm.com>
17. **[12-04 12:02]** Re: [PATCH v3 1/9] arm64: Repaint ID_AA64MMFR2_EL1.IDS description
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[12-04 12:06]** Re: [PATCH v3 8/9] KVM: arm64: pkvm: Report optional ID register traps with a 0x18 syndrome
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[12-05 14:02]** Re: [PATCH v3 6/9] KVM: arm64: Force trap of GMID_EL1 when the guest
 doesn't have MTE
   - 发件人: Yao Yuan <yaoyuan@linux.alibaba.com>
20. **[12-05 14:10]** Re: [PATCH v3 4/9] KVM: arm64: Handle FEAT_IDST for sysregs without
 specific handlers
   - 发件人: Yao Yuan <yaoyuan@linux.alibaba.com>
21. **[12-05 14:25]** Re: [PATCH v3 5/9] KVM: arm64: Handle CSSIDR2_EL1 and SMIDR_EL1 in a
 generic way
   - 发件人: Yao Yuan <yaoyuan@linux.alibaba.com>

---

### Thread 4: [PATCH v8 00/13] Direct Map Removal Support for guest_memfd

**📧 邮件数**: 18 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 5 Dec 2025 16:57:45 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个名为“[PATCH v8 00/13] Direct Map Removal Support for guest_memfd”的补丁系列，旨在为 KVM 的 guest_memfd 提供直接映射移除的支持，以增强对 Spectre 风格的攻击的防护。

**原始补丁内容**：
该补丁系列的核心是扩展 guest_memfd 的功能，使其能够从主机内核的直接映射中移除其内存。这种移除可以防止通过直接映射进行的投机执行攻击，确保虚拟机的内存不被恶意读取。

**历史讨论要点**：
之前的讨论主要集中在补丁设计的细节上，包括如何实现直接映射的移除，以及与现有的 memfd_secret 功能的交互。补丁的设计经过了多次迭代，针对不同架构（如 x86 和 ARM）的支持进行了调整。

**本周的新讨论与进展**：
本周的讨论中，参与者对补丁的具体实现进行了深入探讨，包括对 TLB 刷新的必要性、错误处理机制的建议，以及对接口设计的改进意见。Dave Hansen 提出了对直接映射操作导出到模块的担忧，并建议使用更安全的接口来处理映射的移除和恢复。此外，补丁中引入的 GUEST_MEMFD_FLAG_NO_DIRECT_MAP 标志也得到了关注，确保在创建 guest_memfd 时能够正确处理直接映射的移除。

总的来说，本周的讨论进一步推动了补丁的完善，确保其在安全性和功能性上的有效性。

#### 📝 邮件列表

1. **[12-05 16:57]** [PATCH v8 00/13] Direct Map Removal Support for guest_memfd
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
2. **[12-05 16:57]** [PATCH v8 01/13] x86: export set_direct_map_valid_noflush to KVM
 module
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
3. **[12-05 16:58]** [PATCH v8 02/13] x86/tlb: export flush_tlb_kernel_range to KVM module
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
4. **[12-05 16:58]** [PATCH v8 03/13] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
5. **[12-05 16:58]** [PATCH v8 04/13] KVM: guest_memfd: Add stub for
 kvm_arch_gmem_invalidate
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
6. **[12-05 16:58]** [PATCH v8 05/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
7. **[12-05 16:58]** [PATCH v8 06/13] KVM: x86: define
 kvm_arch_gmem_supports_no_direct_map()
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
8. **[12-05 16:59]** [PATCH v8 07/13] KVM: arm64: define
 kvm_arch_gmem_supports_no_direct_map()
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
9. **[12-05 16:59]** [PATCH v8 08/13] KVM: selftests: load elf via bounce buffer
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
10. **[12-05 16:59]** [PATCH v8 09/13] KVM: selftests: set KVM_MEM_GUEST_MEMFD in
 vm_mem_add() if guest_memfd != -1
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
11. **[12-05 16:59]** [PATCH v8 10/13] KVM: selftests: Add guest_memfd based
 vm_mem_backing_src_types
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
12. **[12-05 16:59]** [PATCH v8 11/13] KVM: selftests: cover GUEST_MEMFD_FLAG_NO_DIRECT_MAP
 in existing selftests
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
13. **[12-05 17:00]** [PATCH v8 12/13] KVM: selftests: stuff vm_mem_backing_src_type into
 vm_shape
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
14. **[12-05 17:00]** [PATCH v8 13/13] KVM: selftests: Test guest execution from direct map
 removed gmem
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
15. **[12-05 09:26]** Re: [PATCH v8 01/13] x86: export set_direct_map_valid_noflush to KVM
 module
   - 发件人: Dave Hansen <dave.hansen@intel.com>
16. **[12-05 09:30]** Re: [PATCH v8 05/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Dave Hansen <dave.hansen@intel.com>
17. **[12-05 10:35]** Re: [PATCH v8 03/13] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: John Hubbard <jhubbard@nvidia.com>
18. **[12-07 03:12]** Re: [PATCH v8 00/13] Direct Map Removal Support for guest_memfd
   - 发件人: Brendan Jackman <jackmanb@google.com>

---

### Thread 5: [PATCH 0/4] KVM: arm64: nv: HAF fixes

**📧 邮件数**: 14 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 28 Nov 2025 10:09:42 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 HAF（Host Address Format）修复的补丁系列，共包含四个补丁。

**原始补丁/问题内容**：
补丁的主要目标是修复与 HAF 相关的错误，特别是在软件翻译表遍历器的支持方面。补丁中提到了一些代码段的潜在问题，尤其是在 hyp_set_prot_attr() 函数中关于权限设置的逻辑。

**之前讨论要点**：
在历史讨论中，参与者们指出了 VTCR_EL2（虚拟化控制寄存器）处理中的问题，特别是与 RES0（保留位）相关的处理不当。Marc Zyngier 提出了对 VTCR_EL2 进行全面转换的建议，以提高代码的一致性和可维护性。

**本周的新讨论、进展或结论**：
本周的讨论中，Marc Zyngier 和 Alexandru Elisei 对补丁进行了审查和讨论，确认了补丁的正确性，并提出了一些代码优化建议。Alexandru 对 Marc 的补丁表示认可，并提供了代码审查意见。Joey Gouly 提出了关于 VTCR_EL2 字段的动态行为问题，Marc 解释了这些字段的处理方式，强调它们的动态性。整体来看，补丁得到了积极的反馈，讨论集中在代码的细节和潜在的改进上。

#### 📝 邮件列表

1. **[11-28 10:09]** [PATCH 0/4] KVM: arm64: nv: HAF fixes
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[11-29 14:45]** [PATCH 0/4] KVM: arm64: VTCR_EL2 conversion to feature dependency framework
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[11-29 14:45]** [PATCH 2/4] arm64: Convert VTCR_EL2 to sysreg infratructure
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[11-29 14:45]** [PATCH 4/4] KVM: arm64: Convert VTCR_EL2 to config-driven sanitisation
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[11-30 13:11]** Re: [PATCH 0/4] KVM: arm64: nv: HAF fixes
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[12-01 09:19]** Re: [PATCH 0/4] KVM: arm64: nv: HAF fixes
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[12-03 11:43]** Re: [PATCH 2/4] arm64: Convert VTCR_EL2 to sysreg infratructure
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
8. **[12-03 11:44]** Re: [PATCH 4/4] KVM: arm64: Convert VTCR_EL2 to config-driven
 sanitisation
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
9. **[12-03 13:00]** Re: [PATCH 4/4] KVM: arm64: Convert VTCR_EL2 to config-driven sanitisation
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[12-03 14:03]** Re: [PATCH 4/4] KVM: arm64: Convert VTCR_EL2 to config-driven
 sanitisation
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
11. **[12-03 14:58]** Re: [PATCH 4/4] KVM: arm64: Convert VTCR_EL2 to config-driven sanitisation
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[12-03 15:20]** Re: [PATCH 4/4] KVM: arm64: Convert VTCR_EL2 to config-driven
 sanitisation
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
13. **[12-03 16:17]** Re: [PATCH 4/4] KVM: arm64: Convert VTCR_EL2 to config-driven
 sanitisation
   - 发件人: Joey Gouly <joey.gouly@arm.com>
14. **[12-03 16:43]** Re: [PATCH 4/4] KVM: arm64: Convert VTCR_EL2 to config-driven sanitisation
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 6: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 18 Nov 2025 10:31:40 +0800

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的补丁，主题为“添加对 FEAT_{LS64, LS64_V} 的支持”。该补丁旨在改善对特定硬件特性的支持，尤其是在处理 MMIO 区域和工作队列时。

在历史讨论中，Zhou Wang 和 Arnd Bergmann 讨论了 ST64B 和 ST64BV0 的使用情况。Zhou 提到他们的系统目前只使用 ST64B，因此建议首先将 FEAT_LS64 合并，后续再讨论 FEAT_LS64V 和 FEAT_LS64_ACCDATA 的需求。Arnd 也确认 ST64B 在效率上通常优于 ST64BV，认为可以在特定硬件上只支持 ST64B，而不向用户空间暴露 ST64BV。

在本周的新讨论中，Zhou 表达了对移除 ST64BV 支持的计划表示认可，并确认在用户空间中将始终使用 ST64B 访问专用工作队列，而 ST64BV 则保留给内核使用。这一决定与 x86 架构的处理方式一致，确保了系统的兼容性和效率。整体来看，讨论的进展表明对补丁的支持逐渐达成共识，且计划在未来版本中进一步优化。

#### 📝 邮件列表

1. **[11-18 10:31]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[11-18 08:36]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Arnd Bergmann <arnd@arndb.de>
3. **[11-27 11:51]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
4. **[11-27 16:37]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Arnd Bergmann <arnd@arndb.de>
5. **[12-05 14:47]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
6. **[12-05 08:09]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Arnd Bergmann <arnd@arndb.de>

---

### Thread 7: [PATCH] KVM: Remove subtle "struct kvm_stats_desc" pseudo-overlay

**📧 邮件数**: 4 | **👥 参与者**: 4 | **📅 开始时间**: Fri,  5 Dec 2025 15:26:55 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 的一个补丁，旨在移除 "struct kvm_stats_desc" 的伪叠加结构。该补丁的主要内容是消除 KVM 内部对 kvm_stats_desc 的伪叠加，避免因灵活数组与固定大小数组的混用而导致的编译器警告，同时简化代码的解引用层级。补丁并不意图引入功能性变化。

在历史讨论中，虽然没有具体的补丁讨论记录，但可以推测该问题的提出是为了改善代码的可读性和维护性，解决编译器警告问题。

在本周的新讨论中，补丁得到了多个参与者的认可和支持。Gustavo A. R. Silva 和 Bibo Mao 分别表示已审核并认可该补丁，Anup Patel 也表示支持，特别是在 RISC-V 的上下文中。整体来看，补丁得到了积极的反馈，预计将会被合并。

#### 📝 邮件列表

1. **[12-05 15:26]** [PATCH] KVM: Remove subtle "struct kvm_stats_desc" pseudo-overlay
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[12-06 12:38]** Re: [PATCH] KVM: Remove subtle "struct kvm_stats_desc" pseudo-overlay
   - 发件人: Gustavo A. R. Silva <gustavo@embeddedor.com>
3. **[12-06 16:16]** Re: [PATCH] KVM: Remove subtle "struct kvm_stats_desc" pseudo-overlay
   - 发件人: Bibo Mao <maobibo@loongson.cn>
4. **[12-07 10:44]** Re: [PATCH] KVM: Remove subtle "struct kvm_stats_desc" pseudo-overlay
   - 发件人: Anup Patel <anup@brainfault.org>

---

### Thread 8: [PATCH v2 0/5] Support the FEAT_HDBSS introduced in Armv9.5

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 21 Nov 2025 17:23:37 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于支持 Armv9.5 中引入的硬件脏状态跟踪结构（HDBSS）特性的补丁系列。

1. **原始补丁内容**：Tian Zheng 提出的补丁系列旨在为 HDBSS 特性提供支持，该特性增强了对翻译表描述符脏状态的跟踪，旨在降低检查脏粒子的成本，同时对记录粒子被弄脏的影响最小化。

2. **之前讨论要点**：在历史讨论中，Tian Zheng 提到需要将 VTCR_EL2 转换为 sysreg 基础设施，而不是在现有结构中添加额外的位。Marc Zyngier 对此表示赞同，并指出这是一个合理的方向。

3. **本周的新讨论与进展**：在本周的讨论中，Tian Zheng 提到他注意到 Marc Zyngier 已经在其补丁中将 VTCR_EL2 添加到 sysreg 基础设施中，并表示一旦该补丁合并到主线，他将删除自己本地的定义。这表明双方在补丁开发上达成了一致，推动了 HDBSS 特性的实现进展。

#### 📝 邮件列表

1. **[11-21 17:23]** [PATCH v2 0/5] Support the FEAT_HDBSS introduced in Armv9.5
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
2. **[11-21 17:23]** [PATCH v2 1/5] arm64/sysreg: Add HDBSS related register information
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
3. **[11-22 12:40]** Re: [PATCH v2 1/5] arm64/sysreg: Add HDBSS related register information
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[12-02 14:51]** Re: [PATCH v2 1/5] arm64/sysreg: Add HDBSS related register
 information
   - 发件人: Tian Zheng <zhengtian10@huawei.com>

---

### Thread 9: [PATCH v3 0/3] KVM ARM64 pre_fault_memory

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 19 Nov 2025 15:49:07 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM ARM64 的预故障内存（pre_fault_memory）功能的补丁系列，旨在减少执行过程中的阶段2故障，特别是在内存密集型应用的后复制迁移场景中，以降低延迟。

**原始补丁内容**：Jack Thomson 提出的补丁系列（PATCH v3 0/3）为 ARM64 添加了 KVM_PRE_FAULT_MEMORY 功能的支持，这一功能之前仅在 x86 平台上可用。补丁包括对 KVM_PRE_FAULT_MEMORY ioctl 的支持，以及为 ARM64 启用预故障内存测试（pre_fault_memory_test），使其能够处理不同的来宾页面大小和多种来宾配置。

**之前的讨论要点**：在历史讨论中，补丁的主要内容和目的被详细阐述，强调了在高延迟情况下的应用场景及其重要性。

**本周的新讨论**：Vincent Donnefort 在本周的邮件中提到，在将补丁应用于基础提交（base commit）后，构建失败，并指出 TEST_NPAGES 仍在 delete_slot_worker() 中被使用，可能与并发内存槽删除的测试有关。他询问是否使用了正确的基础提交，或是否需要使用其他版本。

总体来看，讨论集中在补丁的构建问题和对基础提交的确认上，显示出开发过程中对兼容性和功能验证的关注。

#### 📝 邮件列表

1. **[11-19 15:49]** [PATCH v3 0/3] KVM ARM64 pre_fault_memory
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
2. **[11-19 15:49]** [PATCH v3 2/3] KVM: selftests: Enable pre_fault_memory_test for arm64
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
3. **[12-05 17:33]** Re: [PATCH v3 2/3] KVM: selftests: Enable pre_fault_memory_test for
 arm64
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 10: [PATCH v1 0/5] KVM: arm64: Enforce MTE disablement at EL2

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 27 Nov 2025 12:22:05 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下强制禁用 MTE（Memory Tagging Extension）功能的补丁（PATCH v1 0/5）。Fuad Tabba 提出了这个补丁，旨在确保恶意主机无法利用 MTE 攻击虚拟机或 hypervisor。尽管 pKVM（保护虚拟机）从未向受保护的客户机暴露 MTE，但在硬件支持并启用的情况下，MTE 默认仍然可用于较低的异常级别。因此，仅在主机内核中禁用 MTE 并不能物理上禁用硬件中的 MTE。

在历史讨论中，参与者探讨了补丁的必要性及其对 pKVM 的影响，指出虽然有一些针对 pKVM 的修复，但在启用受保护虚拟机的整体计划上仍然缺乏进展。

在本周的新讨论中，Oliver Upton 表达了对 pKVM 修复的困惑，并提到尽管存在一些长期未解决的问题，但他对启用受保护虚拟机的计划仍然感兴趣。Will Deacon 则表示他最近在此方面进行了一些工作，并计划逐步向上游提交相关补丁，同时希望在此过程中继续关注非受保护客户机的修复进展。整体来看，讨论集中在如何推动 pKVM 的实现及其相关修复的必要性上。

#### 📝 邮件列表

1. **[11-27 12:22]** [PATCH v1 0/5] KVM: arm64: Enforce MTE disablement at EL2
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[12-02 14:43]** Re: [PATCH v1 0/5] KVM: arm64: Enforce MTE disablement at EL2
   - 发件人: Oliver Upton <oupton@kernel.org>
3. **[12-05 17:00]** Re: [PATCH v1 0/5] KVM: arm64: Enforce MTE disablement at EL2
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 11: [PATCH] KVM: selftests: Fix core dump in rseq_test

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 24 Nov 2025 15:04:27 +1000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于修复 KVM 自测工具中的核心转储问题，具体涉及到 rseq_test 测试的一个补丁。

1. **原始补丁内容**：Gavin Shan 提出的补丁旨在修复在 rseq_test 中因参数解析循环中缺少 'break' 导致的核心转储问题。该问题源于在处理参数时，尝试从不存在的参数获取延迟值，最终导致程序崩溃。

2. **之前的讨论要点**：在历史邮件中，Gavin 详细描述了问题的根源，并提出了修复方案，即在参数解析循环中添加 'break' 以避免意外的核心转储。该补丁修复了 commit 0297cdc12a87 中引入的错误。

3. **本周的新讨论和进展**：在本周的讨论中，Gavin 再次请求 Sean Christopherson 对补丁进行审查。Sean 随后回复表示已将补丁应用到 kvm-x86 修复分支，并计划在本周晚些时候向 Paolo 提交修复请求，这意味着该补丁将会被纳入即将发布的 6.19-rc1 版本中。

总的来说，本次讨论围绕 KVM 自测工具中的一个关键问题展开，补丁已被接受并将很快发布。

#### 📝 邮件列表

1. **[11-24 15:04]** [PATCH] KVM: selftests: Fix core dump in rseq_test
   - 发件人: Gavin Shan <gshan@redhat.com>
2. **[12-02 09:16]** Re: [PATCH] KVM: selftests: Fix core dump in rseq_test
   - 发件人: Gavin Shan <gshan@redhat.com>
3. **[12-02 09:05]** Re: [PATCH] KVM: selftests: Fix core dump in rseq_test
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 12: [PATCH v4 0/2] arm: add kvm-psci-version vcpu property

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Tue,  2 Dec 2025 17:08:51 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是针对 ARM 架构的 KVM（Kernel-based Virtual Machine）添加一个新的 vcpu 属性，即 `kvm-psci-version`，用于指定 PSCI（Power State Coordination Interface）版本。

**原始 patch/问题的内容**：
该系列补丁旨在通过 KVM_REG_ARM_PSCI_VERSION 固件寄存器为 vcpu 添加一个选项，以请求特定的 PSCI 版本。这一功能的主要用例是支持在默认 PSCI 版本不同的主机内核之间进行迁移。

**之前讨论要点**：
在之前的讨论中，开发者们对补丁进行了多次迭代，主要集中在变量命名、功能实现的正确性以及与未来内核版本的兼容性等方面。开发者们对补丁的反馈积极，提出了多项改进建议。

**本周的新讨论、进展或结论**：
本周的讨论主要集中在补丁的最终版本上，开发者 Sebastian Ott 提交了 v4 版本的补丁，包含了对 PSCI 版本 1.2 和 1.3 的常量定义，并详细描述了如何通过 `kvm-psci-version` 属性覆盖默认的 PSCI 版本（截至内核 v6.13 为 PSCI v1.3）。补丁得到了 Eric Auger 的认可（R-B），并针对如何处理不同版本的 PSCI 进行了详细的代码实现和注释。整体来看，补丁的功能和实现得到了进一步完善，预计将为 KVM 的 ARM 支持带来更好的灵活性。

#### 📝 邮件列表

1. **[12-02 17:08]** [PATCH v4 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[12-02 17:08]** [PATCH v4 1/2] target/arm/kvm: add constants for new PSCI versions
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[12-02 17:08]** [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 13: [PATCH] KVM: arm64: Prevent FWD_TO_USER of SMCCC to pKVM

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 01 Dec 2025 18:19:52 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 SMCCC（Secure Monitor Call Convention）调用的处理，特别是防止在受保护虚拟机（pKVM）中将这些调用转发到用户空间的补丁。

**原始补丁内容**：Pierre-Clément Tosi 提出的补丁旨在防止在受保护虚拟机中将 SMCCC 调用转发到用户空间，以避免在处理这些调用时出现混淆情况。补丁中建议保留特定的函数ID范围，以确保不会与未来的扩展发生冲突。

**之前讨论要点**：在之前的讨论中，参与者对补丁的必要性和影响进行了探讨。Marc Zyngier 表达了对完全阻止超调用到达用户空间的担忧，认为某些关键超调用（如 MIDR/REVIDR/AIDR）应当允许通过用户空间处理。

**本周新讨论与进展**：本周的讨论中，Marc Zyngier 对补丁进行了快速审查，并建议将补丁限制在特定的函数ID和“调用UID查询”上。Pierre-Clément Tosi 赞同这一建议，并强调不应限制某些关键超调用，以确保 KVM 的用户API能够得到支持。最终，双方达成一致，将在补丁的后续版本中进行相应调整。

#### 📝 邮件列表

1. **[12-01 18:19]** [PATCH] KVM: arm64: Prevent FWD_TO_USER of SMCCC to pKVM
   - 发件人: =?utf-8?q?Pierre-Cl=C3=A9ment_Tosi?= <ptosi@google.com>
2. **[12-01 18:48]** Re: [PATCH] KVM: arm64: Prevent FWD_TO_USER of SMCCC to pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[12-01 19:58]** Re: [PATCH] KVM: arm64: Prevent FWD_TO_USER of SMCCC to pKVM
   - 发件人: =?utf-8?Q?Pierre-Cl=C3=A9ment?= Tosi <ptosi@google.com>

---

### Thread 14: [PATCH v8 26/28] KVM: arm64: Add hyp_enter/hyp_exit events to pKVM hyp

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Sun, 30 Nov 2025 19:00:52 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 KVM（Kernel-based Virtual Machine）中为 arm64 架构添加 hyp_enter/hyp_exit 事件的补丁（PATCH v8 26/28）。该补丁旨在从时间角度记录进入和退出虚拟机监控器（hypervisor）的事件。

在历史讨论中，Vincent Donnefort 提出了对补丁的反对意见，认为不应在未通知的情况下覆盖现有内核构造。他建议定义一个 KVM 特定的包装，而不是将不同的事件（如 SMC 调用和 ERET 返回）归类为相同的“退出”事件。

在本周的新讨论中，Marc Zyngier 和 Vincent Donnefort 继续探讨该补丁的有效性。Marc 表示，这些事件的目的是为了记录进入和退出 hypervisor 的时间，并提到 ACK 中已有其他事件可以提供进入或退出的原因。他愿意在补丁完成后添加更多事件。相对而言，Vincent 对此表示不满，认为当前的实现使得所有入口和出口点相等，缺乏实用性，建议去掉这些事件并实现更有意义的功能。

总体来看，本周的讨论集中在补丁的有效性和设计选择上，双方对如何处理事件的分类和实用性存在明显分歧。

#### 📝 邮件列表

1. **[11-30 19:00]** Re: [PATCH v8 26/28] KVM: arm64: Add hyp_enter/hyp_exit events to pKVM hyp
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[12-01 16:04]** Re: [PATCH v8 26/28] KVM: arm64: Add hyp_enter/hyp_exit events to
 pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[12-01 16:33]** Re: [PATCH v8 26/28] KVM: arm64: Add hyp_enter/hyp_exit events to pKVM hyp
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 15: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct
 map

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 5 Dec 2025 17:23:22 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）中的一个补丁，具体是针对 `guest_memfd` 的功能扩展，目的是添加一个标志以从直接映射中移除内存区域。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁旨在优化内存管理，特别是在处理虚拟机的内存映射时。补丁的核心问题是如何在不影响 ARM 架构的情况下，避免不必要的 TLB（转换后备页表）刷新。

在本周的新讨论中，Nikita Kalyazin 针对补丁进行了内部测试，发现第二次调用 `flush_tlb_kernel_range()` 会引入与第一次相似的延迟，尽管从直觉上看这应该是一个无操作的过程。他表示不确定如何在保持代码架构无关的情况下安全地避免第二次刷新，并考虑寻求其他开发者的建议。尽管如此，他认为从功能的角度来看并没有问题。

此外，Nikita 还提到他在 v8 上运行了 `set_memory_region_test` 测试，并在做了少量配置修改后未能重现之前的失败情况，询问其他参与者是否有时间进行测试以确认问题是否依然存在。

#### 📝 邮件列表

1. **[12-05 17:23]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
2. **[12-05 17:24]** Re: [PATCH v7 12/12] KVM: selftests: Test guest execution from direct
 map removed gmem
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>

---

### Thread 16: [PATCH 00/10] KVM: selftests: Convert to kernel-style types

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 3 Dec 2025 16:04:47 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 自测工具的一个补丁（PATCH 00/10），旨在将其转换为内核风格的类型。该补丁的具体内容和实现细节在邮件中并未详细说明。

在之前的讨论中，参与者 Sean Christopherson 表达了对补丁的关注，并表示由于即将到来的 LPC（Linux Plumbers Conference），他在 6.19 合并窗口关闭之前无法发布新版本的补丁。他提到该补丁的优先级较低，因此可以考虑等待下一个 LTS（长期支持）版本再进行合并。

在本周的新讨论中，David Matlack 对 Sean 的回复表示感谢，并确认了对补丁的审查进展。总体来看，目前的讨论主要集中在补丁的合并时机上，参与者们一致认为可以推迟到下一个 LTS 版本进行处理。

#### 📝 邮件列表

1. **[12-03 16:04]** Re: [PATCH 00/10] KVM: selftests: Convert to kernel-style types
   - 发件人: David Matlack <dmatlack@google.com>

---

### Thread 17: [PATCH v2 2/2] KVM: arm64: vgic: Hoist SGI/PPI alloc from
 vgic_init() to kvm_create_vgic()

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue,  2 Dec 2025 00:35:50 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 VGIC（Virtual Generic Interrupt Controller）相关的一个补丁，具体是将 SGI（Software Generated Interrupt）和 PPI（Private Peripheral Interrupt）的分配从 `vgic_init()` 函数移至 `kvm_create_vgic()` 函数。

历史讨论部分没有提供具体的背景信息，因此我们无法得知之前的讨论要点。

在本周的新讨论中，参与者 Changyuan Lyu 对该补丁提出了担忧。他指出，如果用户空间在 VGIC 创建后但在通过 `KVM_DEV_ARM_VGIC_CTRL_INIT` 初始化之前创建 VCPU，可能会导致问题。具体来说，VCPU 的 `MPIDR_EL1` 寄存器在创建时尚未赋值，而在调用 `KVM_ARM_VCPU_INIT` 时才会被填充。因此，如果按照当前补丁的逻辑，所有 VCPU 必须在 VGIC 创建之前完成创建和初始化，否则会导致 `irq->mpidr` 被赋值为未初始化的值。

Changyuan 请求确认他的理解是否正确，显示出对补丁潜在问题的关注。整体来看，本周的讨论集中在补丁可能引发的顺序依赖问题上。

#### 📝 邮件列表

1. **[12-02 00:35]** Re: [PATCH v2 2/2] KVM: arm64: vgic: Hoist SGI/PPI alloc from
 vgic_init() to kvm_create_vgic()
   - 发件人: Changyuan Lyu <changyuanl@google.com>

---

### Thread 18: [PATCH v2] KVM: arm64: Prevent FWD_TO_USER of SMCCC to pKVM

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 01 Dec 2025 21:26:42 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的一个补丁，旨在防止在受保护虚拟机（pKVM）中将 SMCCC（Secure Monitor Call Convention Calls）调用转发给用户空间。

**原始补丁内容**：
补丁的主要目的是防止受保护虚拟机中的 HVC（Hypervisor Virtual Call）和 SMC（Secure Monitor Call）通过 pKVM 接口转发到用户空间。由于在 pKVM 中，EL2（异常级别2）处理这些调用，可能导致 EL1（异常级别1）无法正确退出到 EL0（异常级别0），从而造成混淆。因此，补丁禁止了受保护虚拟机对特定 SMCCC 调用的注册。

**之前讨论要点**：
由于邮件中没有提供历史讨论的内容，无法总结之前的讨论要点。

**本周新讨论与进展**：
本周的讨论主要集中在补丁的具体实现上。补丁的更新版本（v2）限制了 pKVM HVCs 和 "Call UID Query" 的范围，并更新了相关文档，移除了对 KVM_VM_TYPE_ARM_PROTECTED 的提及。补丁通过在 KVM 的 SMCCC 过滤器中插入特定的调用范围，确保用户空间无法注册处理这些调用，从而避免潜在的安全隐患和混淆。邮件中还提供了补丁的代码变更和相关文档的更新信息。

#### 📝 邮件列表

1. **[12-01 21:26]** [PATCH v2] KVM: arm64: Prevent FWD_TO_USER of SMCCC to pKVM
   - 发件人: =?utf-8?q?Pierre-Cl=C3=A9ment_Tosi?= <ptosi@google.com>

---

### Thread 19: [PATCH] KVM: arm64: Use ARM_SMCCC_OWNER_ARCH in place of 0

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 01 Dec 2025 18:21:09 +0000

#### 🤖 AI 总结

本邮件讨论的主题是一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主要内容是将代码中硬编码的值 0 替换为自文档化的宏 ARM_SMCCC_OWNER_ARCH，以提高代码的可读性和可维护性。

在历史讨论中，虽然没有具体的前期讨论记录，但可以推测出此补丁旨在优化现有代码，使其更符合最佳实践。使用自文档化的宏可以帮助开发者更容易理解代码的意图，减少潜在的错误。

本周的讨论中，Pierre-Clément Tosi 提交了该补丁，并详细说明了修改的具体内容，包括在 `arch/arm64/kvm/hypercalls.c` 文件中对多个地方进行了相应的替换。补丁的具体改动包括在定义 SMC32 和 SMC64 的范围时，将原来的 0 替换为 ARM_SMCCC_OWNER_ARCH。此补丁已被签名并准备好进行进一步的审查和合并。

总体来看，本周的进展是补丁的提交，标志着对 KVM arm64 代码的一个小但重要的改进。

#### 📝 邮件列表

1. **[12-01 18:21]** [PATCH] KVM: arm64: Use ARM_SMCCC_OWNER_ARCH in place of 0
   - 发件人: =?utf-8?q?Pierre-Cl=C3=A9ment_Tosi?= <ptosi@google.com>

---

## 📌 Selftest

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v3 07/10] arm64: selftest: update test for
 running at EL2

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 2 Dec 2025 10:16:42 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于更新 ARM64 自测试以支持在 EL2 级别运行的补丁（PATCH v3 07/10）。该补丁旨在改进当前的自测试代码，使其能够在 EL2 级别正确运行。

在历史讨论中，虽然没有具体的邮件记录，但可以推测之前的讨论涉及如何更有效地检查异常处理程序的执行级别，以及如何优化代码结构以减少条件编译指令（#ifdef）的使用。

在本周的新讨论中，参与者 Eric Auger 和 Joey Gouly 针对补丁的具体实现进行了深入交流。Eric 提出了建议，认为可以在 `check_regs()` 函数中直接使用 `current_level()`，以避免使用条件编译。Joey 则回应称，无法将其移入 `check_regs()`，因为该函数需要检查处理程序的异常级别是否符合预期。随后，Joey 提出了一个未测试的代码修改建议，旨在在多个检查函数中直接设置 `expected_level` 为当前级别，从而简化代码结构。最终，Eric 表达了对这个修改方案的认可。

总结而言，本周的讨论集中在如何优化自测试代码的实现上，参与者们通过具体的代码示例探讨了减少条件编译的可能性，并达成了一致意见。

#### 📝 邮件列表

1. **[12-02 10:16]** Re: [kvm-unit-tests PATCH v3 07/10] arm64: selftest: update test for
 running at EL2
   - 发件人: Eric Auger <eric.auger@redhat.com>
2. **[12-02 12:21]** Re: [kvm-unit-tests PATCH v3 07/10] arm64: selftest: update test for
 running at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
3. **[12-02 13:30]** Re: [kvm-unit-tests PATCH v3 07/10] arm64: selftest: update test for
 running at EL2
   - 发件人: Eric Auger <eric.auger@redhat.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 updates for 6.19

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 1 Dec 2025 12:10:55 -0800

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 在 6.19 版本的更新内容。

1. **原始 patch/问题的内容**：
   本次更新主要包括对 KVM/arm64 的多个重要改进，如支持用户空间处理同步外部中止（SEA）、对 VGIC 列寄存器处理的重大重构、支持 FEAT_XNX 和 FEAT_HAF 特性、允许页表销毁时重新调度等。

2. **之前的讨论要点**：
   之前的讨论未在本邮件中提及，主要集中在对 6.19 版本的准备和更新内容的整合上。

3. **本周的新讨论、进展或结论**：
   本周的讨论主要由 Oliver Upton 提出，他在假期后提交了 6.19 版本的更新内容，并解决了与 6.18 版本中 Marc 提交的修复之间的轻微冲突。Paolo Bonzini 随后确认已成功拉取这些更新，表示感谢。整体来看，本周的进展顺利，更新内容已准备就绪。

#### 📝 邮件列表

1. **[12-01 12:10]** [GIT PULL] KVM/arm64 updates for 6.19
   - 发件人: Oliver Upton <oupton@kernel.org>
2. **[12-02 18:36]** Re: [GIT PULL] KVM/arm64 updates for 6.19
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Discussion

共 7 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support

**📧 邮件数**: 6 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 27 Nov 2025 11:04:43 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 arm64 架构的 KVM 单元测试的补丁（PATCH v3 00/10），主要集中在 EL2 支持的实现上。

在历史讨论中，参与者 Eric Auger 和 Joey Gouly 讨论了在设置 EL2=1 时迁移测试失败的问题。Eric 提到迁移测试在完成后会在第一次中断时出现问题，Joey 表示会进一步调查并确认这个问题。最终，Joey 发现了问题的根源，并提出了修改建议，主要是设置 SCTLR_EL1 的值，以解决之前未能解决的错误。

在本周的新讨论中，Andrew Jones 建议在补丁系列上运行 checkpatch 工具，以确保代码风格符合内核的标准，并指出了 C++ 注释的问题。Joey 随后确认已运行 checkpatch，并修复了一些代码风格问题，尽管该工具并未对 C++/C99 注释发出警告。他表示将把使用的 C++ 注释改为多行风格，以符合更好的编码规范。

总体而言，本周的讨论主要集中在代码风格的改进和确保补丁的质量上。

#### 📝 邮件列表

1. **[11-27 11:04]** Re: [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support
   - 发件人: Eric Auger <eric.auger@redhat.com>
2. **[11-27 11:08]** Re: [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support
   - 发件人: Joey Gouly <joey.gouly@arm.com>
3. **[11-27 13:04]** Re: [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support
   - 发件人: Eric Auger <eric.auger@redhat.com>
4. **[11-27 14:52]** Re: [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support
   - 发件人: Joey Gouly <joey.gouly@arm.com>
5. **[12-01 17:16]** Re: [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
6. **[12-02 14:22]** Re: [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

### Thread 2: [kvm-unit-tests PATCH v3 09/10] arm64: run at EL2 if supported

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 2 Dec 2025 11:35:25 +0100

#### 🤖 AI 总结

本周讨论的主题是关于一个针对 KVM 单元测试的补丁，标题为“[kvm-unit-tests PATCH v3 09/10] arm64: run at EL2 if supported”。该补丁旨在支持在 ARM64 架构上以 EL2（异常级别 2）运行，以增强虚拟化性能和兼容性。

在历史讨论中，未提供具体的背景信息或之前的讨论内容，因此我们无法详细了解该补丁的前期讨论情况。

本周的讨论中，参与者 Eric Auger 对该补丁进行了审阅，并表示支持，标记为“Reviewed-by”。这表明该补丁得到了积极的反馈，可能会进入进一步的审查或合并阶段。

总体来看，本周的讨论主要集中在对补丁的审阅和认可上，显示出社区对该补丁的支持态度。

#### 📝 邮件列表

1. **[12-02 11:35]** Re: [kvm-unit-tests PATCH v3 09/10] arm64: run at EL2 if supported
   - 发件人: Eric Auger <eric.auger@redhat.com>

---

### Thread 3: [kvm-unit-tests PATCH v3 08/10] arm64: pmu: count EL2 cycles

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 2 Dec 2025 11:31:36 +0100

#### 🤖 AI 总结

本邮件主题为“[kvm-unit-tests PATCH v3 08/10] arm64: pmu: count EL2 cycles”，涉及对 ARM64 架构下性能监控单元（PMU）在 EL2 模式下的周期计数功能的补丁。

在本周的新讨论中，参与者 Eric Auger 对该补丁进行了审核，并表示已通过（Reviewed-by）。这表明补丁在技术上得到了认可，可能会进入下一步的合并流程。

由于本邮件没有提供历史讨论的内容，因此无法提供之前的讨论要点。整体来看，本周的进展主要是补丁审核通过，标志着该功能的实现向前迈出了重要一步。

#### 📝 邮件列表

1. **[12-02 11:31]** Re: [kvm-unit-tests PATCH v3 08/10] arm64: pmu: count EL2 cycles
   - 发件人: Eric Auger <eric.auger@redhat.com>

---

### Thread 4: [kvm-unit-tests PATCH v3 06/10] arm64: micro-bench: use smc when
 at EL2

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 2 Dec 2025 10:11:10 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于对 KVM 单元测试的一个补丁（PATCH v3 06/10），该补丁旨在优化 ARM64 架构下在 EL2 级别使用 SMC（Secure Monitor Call）进行微基准测试。

在历史讨论中，未提供具体的背景信息或之前的讨论内容，因此我们无法得知该补丁的详细背景或之前的争论点。

在本周的新讨论中，参与者 Eric Auger 对补丁进行了审核，并表示已通过（Reviewed-by）。这表明补丁在技术上得到了认可，可能会在后续的开发中被采纳。

总结而言，本周的讨论主要集中在对该补丁的审核上，虽然没有提供历史讨论的详细信息，但补丁的审核通过显示出其在社区中的认可度。

#### 📝 邮件列表

1. **[12-02 10:11]** Re: [kvm-unit-tests PATCH v3 06/10] arm64: micro-bench: use smc when
 at EL2
   - 发件人: Eric Auger <eric.auger@redhat.com>

---

### Thread 5: [kvm-unit-tests PATCH v3 05/10] arm64: micro-bench: fix timer IRQ

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 2 Dec 2025 09:36:51 +0100

#### 🤖 AI 总结

本邮件主题为“[kvm-unit-tests PATCH v3 05/10] arm64: micro-bench: fix timer IRQ”，主要讨论了针对 arm64 架构的微基准测试中定时器中断（IRQ）修复的补丁。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁旨在解决与 arm64 微基准测试相关的定时器中断问题，以提高测试的准确性和可靠性。

在本周的新讨论中，Eric Auger 对该补丁进行了审查并表示认可，确认了补丁的有效性。这表明补丁得到了积极的反馈，并可能在后续的开发中被采纳。

总体来看，本周的讨论主要集中在对补丁的审查和确认上，显示出社区对改进 arm64 微基准测试的持续关注。

#### 📝 邮件列表

1. **[12-02 09:36]** Re: [kvm-unit-tests PATCH v3 05/10] arm64: micro-bench: fix timer IRQ
   - 发件人: Eric Auger <eric.auger@redhat.com>

---

### Thread 6: [kvm-unit-tests PATCH v3 04/10] arm64: timer: use hypervisor
 timers when at EL2

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 2 Dec 2025 09:36:27 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 EL2 级别下使用虚拟化定时器的补丁（PATCH v3 04/10），主要针对 arm64 架构的 KVM 单元测试。补丁的目的是在 EL2 级别时使用 hypervisor 定时器，以提高系统的定时精度和性能。

在之前的讨论中，虽然没有具体的邮件记录，但可以推测出该补丁的提出是为了优化 KVM 的定时器管理，确保在不同的执行级别下能够正确使用相应的定时器。

在本周的新讨论中，参与者 Eric Auger 对补丁进行了审查，并提出了一个小的修改建议，建议将一个断言移动到条件判断中，以确保在当前级别为 EL1 时的逻辑处理更加清晰。Eric 表示已对该补丁进行了审核并给予了认可（Reviewed-by）。

总的来说，本周的讨论主要集中在对补丁的细节审查和小幅修改建议上，显示出社区对提升 KVM 性能的持续关注。

#### 📝 邮件列表

1. **[12-02 09:36]** Re: [kvm-unit-tests PATCH v3 04/10] arm64: timer: use hypervisor
 timers when at EL2
   - 发件人: Eric Auger <eric.auger@redhat.com>

---

### Thread 7: [kvm-unit-tests PATCH v3 10/10] arm64: add EL2 environment
 variable

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 1 Dec 2025 17:34:57 -0600

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 单元测试中为 arm64 架构添加 EL2 环境变量的补丁（patch）。该补丁旨在增强测试框架的灵活性，使其能够更好地支持 EL2 模式的测试。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了改进现有的测试功能，以便更好地适应 arm64 架构的需求。

在本周的新讨论中，参与者 Andrew Jones 对补丁提出了建议，要求在支持的环境变量中加入对 'y' 和 'Y' 的支持，以便用户可以通过命令行参数（如 'EL2=y run_tests.sh -g ...'）来更方便地运行测试。这一建议旨在提高用户体验，使得测试执行更加灵活和直观。

总体来看，本周的讨论集中在补丁的功能扩展上，进一步推动了对 arm64 EL2 环境变量支持的完善。

#### 📝 邮件列表

1. **[12-01 17:34]** Re: [kvm-unit-tests PATCH v3 10/10] arm64: add EL2 environment
 variable
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

## 📌 Other

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v4 00/11] arm64: EL2 support

**📧 邮件数**: 15 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  4 Dec 2025 14:23:27 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 KVM 单元测试的补丁系列，主要目的是增加对 EL2（异常级别 2）的支持。

1. **原始补丁内容**：补丁系列（PATCH v4 00/11）旨在为 KVM 单元测试添加在 EL2 下运行的支持。补丁包括一系列对 ARM64 代码的修改，涉及初始化、定时器、性能监控单元（PMU）等方面。

2. **历史讨论要点**：历史讨论中，参与者对补丁进行了多次审查和反馈，提出了对代码风格和功能实现的建议，例如修复检查工具（checkpatch.pl）的问题、调整环境变量的命名等。

3. **本周新讨论及进展**：本周的讨论中，Joey Gouly 提交了多个补丁，主要包括：
   - 确保在启动时设置 SCTLR_EL1 的已知值，以保持主核和从核的一致性。
   - 在 EL2 启动时，若不支持 VHE（虚拟化扩展），则降级到 EL1。
   - 完善 EFI 启动时的 SCTLR_ELx 初始化。
   - 在 EL2 中使用超管定时器，并修复定时器 IRQ 的处理。
   - 更新自测代码以适应 EL2 的运行环境。
   - 添加 EL2 环境变量支持，使得 QEMU/kvmtool 可以在 EL2 下启动。

此外，Andrew Jones 对部分补丁进行了审查，提出了改进建议，强调了代码的可维护性和一致性。整体上，本周的讨论集中在补丁的细节和实现效果上，推动了对 EL2 支持的进一步完善。

#### 📝 邮件列表

1. **[12-04 14:23]** [kvm-unit-tests PATCH v4 00/11] arm64: EL2 support
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[12-04 14:23]** [kvm-unit-tests PATCH v4 01/11] arm64: set SCTLR_EL1 to a known value for secondary cores
   - 发件人: Joey Gouly <joey.gouly@arm.com>
3. **[12-04 14:23]** [kvm-unit-tests PATCH v4 02/11] arm64: drop to EL1 if booted at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
4. **[12-04 14:23]** [kvm-unit-tests PATCH v4 03/11] arm64: efi: initialise SCTLR_ELx fully
   - 发件人: Joey Gouly <joey.gouly@arm.com>
5. **[12-04 14:23]** [kvm-unit-tests PATCH v4 04/11] arm64: efi: initialise the EL
   - 发件人: Joey Gouly <joey.gouly@arm.com>
6. **[12-04 14:23]** [kvm-unit-tests PATCH v4 05/11] arm64: timer: use hypervisor timers when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
7. **[12-04 14:23]** [kvm-unit-tests PATCH v4 06/11] arm64: micro-bench: fix timer IRQ
   - 发件人: Joey Gouly <joey.gouly@arm.com>
8. **[12-04 14:23]** [kvm-unit-tests PATCH v4 07/11] arm64: micro-bench: use smc when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
9. **[12-04 14:23]** [kvm-unit-tests PATCH v4 08/11] arm64: selftest: update test for running at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
10. **[12-04 14:23]** [kvm-unit-tests PATCH v4 09/11] arm64: pmu: count EL2 cycles
   - 发件人: Joey Gouly <joey.gouly@arm.com>
11. **[12-04 14:23]** [kvm-unit-tests PATCH v4 10/11] arm64: run at EL2 if supported
   - 发件人: Joey Gouly <joey.gouly@arm.com>
12. **[12-04 14:23]** [kvm-unit-tests PATCH v4 11/11] arm64: add EL2 environment variable
   - 发件人: Joey Gouly <joey.gouly@arm.com>
13. **[12-04 09:58]** Re: [kvm-unit-tests PATCH v4 01/11] arm64: set SCTLR_EL1 to a known
 value for secondary cores
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
14. **[12-04 11:09]** Re: [kvm-unit-tests PATCH v4 08/11] arm64: selftest: update test for
 running at EL2
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
15. **[12-04 11:17]** Re: [kvm-unit-tests PATCH v4 11/11] arm64: add EL2 environment
 variable
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

